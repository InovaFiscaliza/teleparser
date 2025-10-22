#!/bin/bash
set -e
for semana in {65..69}; do
    uv run -p pypy3 src/teleparser/main.py "./data/vm_win/Semana${semana}/tim/ericsson" -s "data/cdr_traduzido/Semana${semana}/tim/ericsson" -n 8 --tipo ericsson_voz_optimized \
    && uv run -p pypy3 src/teleparser/main.py "./data/vm_win/Semana${semana}/tim/ericsson" -s "data/cdr_traduzido/Semana${semana}/tim/ericsson" -n 8 --tipo ericsson_voz

    
done

for semana in {65..69}; do
    uv run -p pypy3 src/teleparser/main.py "./data/vm_win/Semana${semana}/vivo/ericsson" -s "data/cdr_traduzido/Semana${semana}/vivo/ericsson" -n 1 --tipo ericsson_voz_optimized \
    && uv run -p pypy3 src/teleparser/main.py "./data/vm_win/Semana${semana}/vivo/ericsson" -s "data/cdr_traduzido/Semana${semana}/vivo/ericsson" -n 1 --tipo ericsson_voz


done

