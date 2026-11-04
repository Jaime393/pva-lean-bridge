#!/usr/bin/env python3
"""Extract a formalization backlog. Never replace a claim with a proof of True."""
import argparse
import hashlib
import json
from pathlib import Path
import re

MAX_BYTES = 2 * 1024 * 1024
PATTERN = re.compile(r"\\begin\{(theorem|lemma|definition|proposition)\}(.*?)\\end\{\1\}", re.S)


def extract_theorems(tex_path):
    path = Path(tex_path)
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BYTES:
        raise ValueError("bounded regular LaTeX source required")
    text = path.read_text(encoding="utf-8")
    text = "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())
    return [(kind, body.strip()) for kind, body in PATTERN.findall(text)]


def gen_lean_skeleton(name, body):
    # Every untrusted source line remains a comment, including multiline statements.
    comments = "\n".join("-- " + line for line in body.splitlines())
    return ("-- Formalization backlog, NOT a proof of the original statement.\n"
            f"-- Content ID: {name}\n"
            "-- TODO: supply a formal proposition, definitions and proof.\n"
            "-- No theorem, axiom, sorry or trivial proof is generated.\n"
            + comments + "\n")


def build_backlog(tex_path, output=None):
    path = Path(tex_path)
    pairs = extract_theorems(path)
    raw = path.read_bytes()
    statements = {}
    for kind, body in pairs:
        digest = hashlib.sha256((kind + "\0" + body).encode()).hexdigest()
        if digest in statements:
            statements[digest]["occurrences"] += 1
        else:
            statements[digest] = {"statement_id": "sha256:" + digest, "kind": kind,
                                  "source": body, "occurrences": 1,
                                  "file": "statement_" + digest + ".lean",
                                  "formal_statement_supplied": False, "proof_supplied": False}
    report = {"schema": "pva.formalization-backlog/v1",
              "source_filename": path.name, "source_sha256": hashlib.sha256(raw).hexdigest(),
              "statement_occurrences": len(pairs), "distinct_statements": len(statements),
              "statements": sorted(statements.values(), key=lambda item: item["statement_id"]),
              "lean_compilation_executed": False, "original_claims_proved": False,
              "parser_scope": "Textual supported environments only, not a complete TeX parser.",
              "files_written": False}
    if output is not None:
        target = Path(output)
        if target.is_symlink() or (target.exists() and (not target.is_dir() or any(target.iterdir()))):
            raise ValueError("output must be a fresh or empty non-symlink directory")
        target.mkdir(parents=True, exist_ok=True)
        for item in report["statements"]:
            with (target / item["file"]).open("x", encoding="utf-8") as out:
                out.write(gen_lean_skeleton(item["statement_id"], item["source"]))
        report["files_written"] = True
        with (target / "gaps.json").open("x", encoding="utf-8") as out:
            json.dump(report, out, indent=2, sort_keys=True)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", type=Path, default=Path(__file__).resolve().parent / "paper.tex")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    try:
        result = build_backlog(args.tex, args.out)
    except (OSError, ValueError):
        parser.exit(2, "Blocked: missing/invalid source or output collision; no example or proof invented.\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
