# INVENTARIO — pva-lean-bridge

Repo: `Jaime393/pva-lean-bridge`, rama `main`.
Leído en vivo: 2026-11-09 ~07:42 -05. Los 13 archivos, íntegros.
HEAD: `5007fd55`, 2026-09-10T21:18:35Z. Total: 2 commits.

## Totales

- **13 archivos, 6.894 B.**
- 0 archivos de código Lean compilables verificados (Lean no está instalado aquí; ver CONTENIDO).
- 0 tests. 0 LICENSE.

## Raíz (6 archivos, 2.523 B)

| Archivo | B | Qué es |
|---|---|---|
| `.gitignore` | 9 | Una línea: `*.tar.gz`. |
| `Makefile` | 146 | 4 objetivos (`repro`, `reproduce`, `dev`, `test`); todos corren `cli.py`. |
| `README.md` | 414 | Descripción del puente LaTeX → Lean 4 + ejemplo Navier-Stokes. |
| `cli.py` | 1.611 | El programa: extrae teoremas de LaTeX y genera esqueletos Lean + `gaps.json`. |
| `lakefile.lean` | 50 | `package pva-lean-bridge`, sin dependencias declaradas. |
| `paper.tex` | 293 | Ejemplo LaTeX: 1 teorema (Navier-Stokes Clay) + 1 definición (Sobolev H1). |

## `lean/` (5 archivos, 2.533 B)

| Archivo | B | Qué es |
|---|---|---|
| `KiPhiBeta.lean` | 1.182 | Definiciones K_i, banda de resiliencia, exponente β, axioma falsador. Añadido en el 2.º commit. |
| `NavierStokes.lean` | 718 | Enunciado Clay en Lean 4: 3 `sorry` + teorema `True`. |
| `gaps.json` | 112 | Informe de brechas: 2 teoremas, 3 brechas fijas. |
| `theorem_0_theorem.lean` | 296 | Esqueleto generado por `cli.py` desde `paper.tex` (teorema 0). |
| `theorem_1_definition.lean` | 225 | Esqueleto generado por `cli.py` desde `paper.tex` (definición 1). |

## `scripts/` (1 archivo, 1.611 B)

| Archivo | B | Qué es |
|---|---|---|
| `bridge.py` | 1.611 | Copia byte a byte de `cli.py` (mismo sha256 `e6a5f69b…`, verificado por `cmp`). |

## `.github/workflows/` (1 archivo, 227 B)

| Archivo | B | Qué es |
|---|---|---|
| `pva.yml` | 227 | Workflow: en cada push, instala `click`, corre `cli.py` y lista `lean/`. |

## NO SÉ

- Si el workflow `pva.yml` corrió alguna vez (no hay herramienta aquí para ver ejecuciones de Actions; no se verificó).
- Si `lake build` corrió alguna vez (Lean no está instalado en esta máquina; el `lakefile.lean` no declara dependencias).
