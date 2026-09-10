#!/usr/bin/env python3
# pva-lean-bridge V202 — LaTeX -> Lean4 esqueleto — rho(x)>0
import re, pathlib, click, json
from pathlib import Path

def extract_theorems(tex_path):
    text = Path(tex_path).read_text(errors='ignore')
    # busca \begin{theorem} ... \end{theorem} o \begin{definition}
    pattern = r'\\begin\{(theorem|lemma|definition|proposition)\}(.*?)\\end\{\1\}'
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def gen_lean_skeleton(name, body):
    return f'''import Mathlib

-- {name} extraido de LaTeX
-- TODO: formalizar

theorem {name}_placeholder : True := by
  trivial

-- cuerpo original LaTeX:
-- {body[:200]}...
'''

@click.command()
@click.option("--tex", default="paper.tex", help="Paper LaTeX")
@click.option("--out", default="lean", help="Out dir")
def main(tex, out):
    p = Path(tex)
    if not p.exists():
        print(f"No existe {tex}, creando ejemplo Navier-Stokes")
        Path(tex).write_text(r"\begin{theorem}[Navier-Stokes Clay]\n Existe solucion suave... \end{theorem}")
    thms = extract_theorems(tex)
    Path(out).mkdir(exist_ok=True)
    for i,(kind,body) in enumerate(thms):
        name = f"theorem_{i}_{kind}"
        (Path(out)/f"{name}.lean").write_text(gen_lean_skeleton(name, body))
    print(f"Generados {len(thms)} esqueletos en {out}/")
    # genera informe brechas
    report = {"theorems": len(thms), "gaps": ["definir Sobolev", "definir solucion debil", "definir suavidad"]}
    Path(f"{out}/gaps.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
