# pva-lean-bridge

Extractor de una cola de formalización a partir de entornos LaTeX. No transforma una afirmación matemática en un teorema de `True`, ni atribuye una prueba al enunciado original.

```bash
python3 cli.py --tex paper.tex
python3 cli.py --tex paper.tex --out audit-output/backlog
python3 scripts/bridge.py --tex paper.tex
python3 -m unittest discover -s tests -v
```

El reporte usa IDs por contenido, hash de fuente, tipo y ocurrencias. Todos los renglones de fuente generados quedan comentados; no se genera `axiom`, `sorry` ni prueba trivial como sustituto de la afirmación original.

El modo predeterminado no escribe archivos. Una salida explícita debe ser nueva o vacía; no se sobrescribe `lean/` ni se crea un ejemplo cuando falta la entrada.

Los archivos históricos de `lean/`, su configuración y sus `axiom`/`sorry` se conservan como material no validado. No se ejecutó Lean/Mathlib ni se comprobó compilación o prueba formal en esta revisión. El extractor textual no es un parser completo de TeX.
