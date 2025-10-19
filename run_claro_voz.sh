#!/bin/bash
set -e
for semana in {36..69}; do
    uv run -p pypy3 src/teleparser/main.py "./data/vm_win/Semana${semana}/claro/ericsson" -r -s "data/cdr_traduzido/Semana${semana}/claro/ericsson" -n 32 --tipo ericsson_voz_optimized \
    && uv run -p pypy3 src/teleparser/main.py "./data/vm_win/Semana${semana}/claro/ericsson" -s "data/cdr_traduzido/Semana${semana}/claro/ericsson" -n 32 --tipo ericsson_voz
done
