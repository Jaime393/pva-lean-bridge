# pva-lean-bridge V202 — rho(x)>0

Puente LaTeX -> Lean 4 — genera esqueletos Mathlib + informe brechas.

```bash
pip install click
python cli.py --tex paper.tex --out lean
lake build # si tienes Lean 4 + Mathlib
```

Incluye ejemplo `lean/NavierStokes.lean` enunciado Clay — esqueleto vacio — primer paso PVA para Problema del Milenio.

Bloque 2 formalizacion — parte de PVA ecosistema 20 herramientas.
