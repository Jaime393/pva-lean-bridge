# LECTURA — pva-lean-bridge

Repo: Jaime393/pva-lean-bridge, rama main.
Leído en vivo: 2026-11-09 ~07:42 -05 (los 13 archivos, íntegros).

## Qué dice el README (íntegro, 414 B)

> `# pva-lean-bridge V202 — rho(x)>0`
>
> `Puente LaTeX -> Lean 4 — genera esqueletos Mathlib + informe brechas.`
>
> ```bash
> pip install click
> python cli.py --tex paper.tex --out lean
> lake build # si tienes Lean 4 + Mathlib
> ```
>
> `Incluye ejemplo lean/NavierStokes.lean enunciado Clay — esqueleto vacio — primer paso PVA para Problema del Milenio.`
>
> `Bloque 2 formalizacion — parte de PVA ecosistema 20 herramientas.`

## Qué dice `paper.tex` (íntegro, 293 B)

Dos entornos: un teorema (Navier-Stokes Clay: "Sea $u_0$ campo inicial suave divergencia cero. Entonces existe solucion suave global de Navier-Stokes") y una definición (Sobolev H1: "$H^1$ funciones con derivada L2...").

## Qué dice `lean/KiPhiBeta.lean` (cabecera, literal)

> `/-`
> `  MIU V202 — Ki, Φ, β — formalización operacional`
> `  ρ(x) > 0 — Phi 9158.79`
> `  K_i = φ⁻¹ · (D_f / 2.5) · (ℓ_corr / ℓ_0)`
> `  K_i(Φ) ∝ (Φ - Φ_c)^β  β≈0.5`
> `  g_μν = E[∂_μ ln ρ · ∂_ν ln ρ]`
> `-/`

Y el axioma falsador, literal:

> `axiom falsador_blindsight : ∀ Phi Phi_c, Phi > Phi_c → False -- placeholder para medición empírica`

Y el "teorema núcleo", literal:

> `theorem identidad_nomologica : ∀ x, True := fun _ => trivial`

## Qué dice `lean/NavierStokes.lean` (literal)

Los tres placeholders usan `sorry`:

> `def SobolevH1 := sorry`
> `def WeakSolution := sorry`
> `def SmoothCondition := sorry`
>
> `theorem navier_stokes_existence : True := by`
> `  trivial`

Y el TODO, literal:

> `-- 1. Definir H^1, L^2, espacios de divergencia cero`
> `-- 2. Definir solucion debil con presion`
> `-- 3. Definir condicion de suavidad y acotamiento`
> `-- 4. Referencias: Fefferman 2000 Clay description`

## Qué dice `lean/gaps.json` (íntegro, 112 B)

```json
{
  "theorems": 2,
  "gaps": [
    "definir Sobolev",
    "definir solucion debil",
    "definir suavidad"
  ]
}
```

## Qué dice el workflow `.github/workflows/pva.yml` (íntegro, 227 B)

```yaml
name: PVA lean bridge
on: [push]
jobs:
  pva:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install click
      - run: python cli.py --tex paper.tex --out lean
      - run: ls -R lean
```

## Qué dice el `Makefile` (íntegro, 146 B)

```make
repro:
	python cli.py --tex paper.tex --out lean

reproduce:
	python cli.py --tex paper.tex --out lean

dev:
	python cli.py

test:
	python cli.py
```

## Lo que el repo promete vs lo que muestra

- Promete "genera esqueletos Mathlib + informe brechas": el programa lo hace (ver CONTENIDO, ejecución reproducida).
- Promete "primer paso PVA para Problema del Milenio": el esqueleto existe, vacío por diseño declarado ("esqueleto vacio", "TODO: formalizar").
- Promete "Bloque 2 formalizacion — parte de PVA ecosistema 20 herramientas": la pertenencia al ecosistema PVA consta en el README y en los 6 hermanos `pva-*` (ver FAMILIA).
- El `Makefile` promete un objetivo `test`: corre `cli.py`, no prueba nada. No hay tests en el repo.

## NO SÉ

- De dónde sale "Phi 9158.79" en la cabecera de `KiPhiBeta.lean`: ningún archivo del repo lo deriva ni lo explica.
- Si el workflow corrió alguna vez y qué imprimió (no verificable desde aquí).
