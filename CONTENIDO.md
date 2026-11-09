# CONTENIDO — pva-lean-bridge

Repo: `Jaime393/pva-lean-bridge`, rama `main`.
Leído en vivo 2026-11-09 ~07:42 -05. Todos los números abajo se
calcularon o se leyeron de los archivos del repo, no de memoria.

## Qué hace

Es un puente LaTeX → Lean 4: lee un `.tex`, extrae los entornos
`theorem` / `lemma` / `definition` / `proposition` con una expresión
regular, y por cada uno escribe un esqueleto Lean que importa Mathlib
y declara un teorema `True := by trivial`. Además escribe un informe
de brechas (`gaps.json`).

## Ejecución reproducida (SÉ, 2026-11-09 ~07:42 -05)

Corrido en local en un venv con `click` 8.5.1, sobre la copia exacta
de `cli.py` y `paper.tex` del repo:

- Salida: `Generados 2 esqueletos en /tmp/pva-lean-check/out/`.
- Generó 3 archivos: `gaps.json` (112 B), `theorem_0_theorem.lean`
  (296 B), `theorem_1_definition.lean` (225 B).
- **Los 3 son byte a byte idénticos a los del repo** (`cmp`):
  `gaps.json`, `theorem_0_theorem.lean` y `theorem_1_definition.lean`
  coinciden con `lean/` del repo. Los archivos comprometidos son el
  producto de correr `cli.py` sobre `paper.tex`.

## Lo que el código realmente hace (leído, no inferido)

- `extract_theorems`: regex `\\begin\{(theorem|lemma|definition|proposition)\}(.*?)\\end\{\1\}`.
  Solo esos 4 entornos. El cuerpo del teorema se recorta a 200
  caracteres en el esqueleto generado.
- `gen_lean_skeleton`: el teorema generado es siempre
  `theorem {name}_placeholder : True := by trivial`. No formaliza nada.
- El informe de brechas es **fijo en el código**:
  `{"theorems": len(thms), "gaps": ["definir Sobolev", "definir solucion debil", "definir suavidad"]}`.
  Solo el conteo `theorems` se deriva del papel; las 3 brechas son
  literales, no se extraen de nada.
- Si `paper.tex` no existe, `cli.py` **lo crea** con un teorema
  Navier-Stokes de ejemplo y sigue. Correr sin papel fabrica el ejemplo.
- `cli.py` y `scripts/bridge.py` son **byte a byte idénticos**
  (1.611 B cada uno, mismo sha256 `e6a5f69b…`, verificado por `cmp`).
  El repo lleva el mismo programa dos veces, en dos rutas.

## Lo que NO prueba ni calcula

- `lean/NavierStokes.lean`: 3 definiciones con `sorry`
  (`SobolevH1`, `WeakSolution`, `SmoothCondition`) y un teorema
  `True := by trivial`. Nada demostrado.
- `lean/KiPhiBeta.lean`: el "teorema núcleo" es
  `∀ x, True := fun _ => trivial`. Nada demostrado.
- El axioma `falsador_blindsight` dice, literal:
  `∀ Phi Phi_c, Phi > Phi_c → False`. Como axioma, de cualquier par
  concreto con `Phi > Phi_c` se deriva `False`. Y `Ki_of_Phi` exige
  precisamente una prueba de `Phi > Phi_c` como argumento. Los dos
  tiran en direcciones opuestas; el archivo no lo resuelve.
- `lakefile.lean` no declara ninguna dependencia (sin `require`),
  mientras los archivos `.lean` hacen `import Mathlib`. Sin Mathlib
  como dependencia, `lake build` no puede resolver el import.

## Aritmética verificada (SÉ, calculada en local)

- `φ^4/2` con φ = 1,618034 da **3,427051** — coincide con el σ = 3,427
  del repo y de los READMEs v150. Con φ = 0,618034 daría 0,073.
  El archivo usa φ = 1,618; el Grimorio llama φ a 0,618. Escalas
  distintas, sin reconciliar en ningún archivo.
- `RAIZ_X = 20·φ^4 − (φ−1)/13` con φ = 1,618034 da **137,034502**;
  el repo escribe 137,034498. Diferencia ~4e-6 (redondeo).
- `K_i` con D_f = 2,5 y ℓ_corr/ℓ_0 = 1 da **0,618** — el propio
  φ⁻¹, en el borde superior de la banda [0,55, 0,62] por construcción.
- "Phi 9158.79" (cabecera de `KiPhiBeta.lean`): sin derivación en
  ningún archivo. NO SÉ de dónde sale.

## Lo que falta (medido, no opinado)

- Sin LICENSE. Sin directorio `tests/` (el objetivo `test` del
  `Makefile` solo corre `cli.py`).
- `repro` y `reproduce` son el mismo comando; `dev` y `test` son el
  mismo comando (`python cli.py` sin argumentos).
- `.gitignore` solo ignora `*.tar.gz`.
- Lean no está instalado en esta máquina (`which lean lake elan`:
  nada; sin `~/.elan`). `lake build` no se ejecutó aquí; NO SÉ si
  corrió alguna vez ni qué dio.
- El workflow `pva.yml` no se verificó corriendo (NO SÉ si corrió).
