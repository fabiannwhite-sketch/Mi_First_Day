# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository structure

This is not a single application — it's a collection of small, independent demo/practice projects, each self-contained in its own top-level folder. There is no shared build system, package manager, or dependency graph between them. When working on one project, treat its folder as the entire scope; nothing here imports across project folders.

Current projects:

- `calculadora_web/` — single-file HTML calculator (see below).
- `identificador_meteoritos/` — single-file HTML app (see below).
- `mediciones_fisicas/` — two standalone Python scripts (see below).

## Web apps (`calculadora_web/`, `identificador_meteoritos/`)

Each is a single `index.html` file with CSS and JavaScript embedded inline (`<style>`/`<script>` in the same file) — no external dependencies, no build step, no bundler. Open the file directly in a browser to run it (double-click, or `file://` URL).

Conventions used across these apps:
- Dark theme, rounded card UI centered on the page, vanilla DOM manipulation (`document.querySelectorAll`, `addEventListener`) — no frameworks.
- UI text and comments are in Spanish, matching the user's language.
- Keep new web apps in this repo self-contained (single HTML file, inline CSS/JS) unless the user asks for a build setup.

## Python scripts (`mediciones_fisicas/`)

- `generador.py` — generates `datos.csv` (50 rows of `tiempo`/`valor` synthetic measurements) using only the standard library (`csv`, `random`).
- `analizador.py` — reads `datos.csv`, computes mean/stdev/max with the `statistics` module, and writes a Markdown summary to `informe.md`.

Run in order: `python generador.py` then `python analizador.py`, from inside `mediciones_fisicas/`.

**Note:** As of this writing, Python is not installed on this machine (only the Microsoft Store stub is present), so these scripts have not been executed/verified end-to-end. Check `python --version` before assuming a working interpreter is available.
