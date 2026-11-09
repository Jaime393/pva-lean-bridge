# FAMILIA — pva-lean-bridge

Repo: `Jaime393/pva-lean-bridge`, rama `main`.
Leído en vivo: 2026-11-09 ~07:42 -05.

## Familia PVA (7 repos, todos head 2026-09-10)

`pva-lean-bridge` es el **Bloque 2, formalización**, del ecosistema
PVA, según su propio README: "parte de PVA ecosistema 20 herramientas".
Los 7 repos `pva-*` tienen su último commit el 2026-09-10:

| Repo | Head | Qué es (según su README) |
|---|---|---|
| `pva-docker-template` | 2026-09-10T16:45:11Z | Plantilla de reproducibilidad (Docker + Make). Minado ola 4 tanda 1. |
| `pva-ledger` | 2026-09-10T17:02:57Z | Registro inmutable (Arweave + Zenodo DOI). En tanda 2. |
| `pva-lean-bridge` | 2026-09-10T21:18:35Z | Puente LaTeX → Lean 4 (este repo). |
| `pva-orchestrator` | 2026-09-10T21:18:59Z | Orquestador: encadena lint + docker + lean + ledger + swarm con un `pva.yml`. En tanda 2. |
| `pva-swarm` | 2026-09-10T21:22:34Z | Validación adversarial distribuida. En tanda 2. |
| `pva-lint` | 2026-09-10T22:29:27Z | Linter PVA con score 0–1. En tanda 3. |
| `pva-api` | 2026-09-10T23:02:53Z | API única (FastAPI o stdlib). En tanda 3. |

## Cruces dentro de la familia

- **El orquestador lo nombra:** el README de `pva-orchestrator`
  encadena "lint + docker + lean + ledger + swarm". Este repo es el
  "lean" de esa cadena. El `Makefile` de `pva-docker-template`
  depende de `pva-lint` solo si está al lado.
- **La fórmula K_i circula:** `Ki = φ⁻¹·(D_f/2.5)·(ℓ_corr/ℓ_0)` con
  banda [0,55, 0,62] aparece en `lean/KiPhiBeta.lean` (este repo),
  en el endpoint `/api/ki` de `pva-api` y en la regla `Ki_band`
  de `pva-lint` (según sus mensajes de commit). Misma fórmula,
  misma banda, tres repos.
- **El σ = 3,427 circula:** `φ^4/2 = 3,427` aparece en este repo y
  en los 4 READMEs `miu-v150-*` (misma familia de números, mismos
  datos TN-14). Los v150 usan φ = 1,618, igual que aquí.
- **El vocabulario "nutriente":** el 2.º commit se llama "nutriente
  formal: Ki Phi Beta". La palabra "nutriente" es la misma de los
  repos `nutriente-*` del 30 de julio (sembrados 20/20) y de la
  semilla `miu-auto-cipher19051997-0` del 7 de noviembre.
- **Duplicación interna:** `cli.py` y `scripts/bridge.py` son el
  mismo programa dos veces (byte a byte idénticos). El commit init
  lo llama `bridge.py`; el README lo llama `cli.py`.

## Cruces fuera de la familia

- **MIU / Grimorio:** el README no cita el Grimorio, pero la
  convención φ difiere: aquí φ = 1,618 (φ^4/2 = 3,427 verificado);
  el Grimorio llama φ a 0,618 (GRIMORIO_TEXTO_COMPLETO.md).
  Ningún archivo reconcilia ambas.
- **Fefferman 2000:** el TODO de `NavierStokes.lean` cita la
  descripción Clay de Fefferman 2000 como referencia. No hay
  bibliografía ni enlace en el repo.
- **Mathlib / Lean 4:** los esqueletos importan Mathlib, pero el
  `lakefile.lean` no lo declara como dependencia. Sin Mathlib
  declarado, el proyecto no compila como está escrito.

## NO SÉ

- Cuáles son las "20 herramientas" del ecosistema PVA (el README
  las nombra como total; solo 7 repos `pva-*` existen bajo Jaime393).
- Si el orquestador (`pva-orchestrator`) llegó a correr este puente
  alguna vez (su `pva.yml` lo encadena; no hay logs en este repo).
- Si algún paper real pasó por este puente (el único `paper.tex`
  es el ejemplo Navier-Stokes que el propio repo trae).
