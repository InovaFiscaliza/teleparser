# uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana43/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_260325 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana43/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana44/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_040425 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana44/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana45/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_080425 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana45/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana46/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_140425 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana46/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana47/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_230425 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana47/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana48/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_280425 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana48/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana49/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_090525 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana49/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana50/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_130525 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana50/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana51/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_220525 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana51/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana52/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_300525 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana52/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana53/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_040625 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana53/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana54/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_120625 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana54/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana55/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_160625 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana55/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana56/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_270625 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana56/claro/volte/ -n 8 \
# && uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana57/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_4G_020725 --tipo ericsson_volte_optimized -s data/cdr_traduzido/Semana57/claro/volte/ -n 8 \

uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana43/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_ERICSSON_260325 --tipo ericsson_voz -s data/cdr_traduzido/Semana43/claro/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana44/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_ERICSSON_040425 --tipo ericsson_voz -s data/cdr_traduzido/Semana44/claro/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana45/Tim/GSM/ --tipo ericsson_voz -s data/cdr_traduzido/Semana45/tim/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana45/Vivo/CDR/ --tipo ericsson_voz -s data/cdr_traduzido/Semana45/vivo/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana45/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_ERICSSON_080425 --tipo ericsson_voz -s data/cdr_traduzido/Semana45/claro/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana46/Tim/GSM/ --tipo ericsson_voz -s data/cdr_traduzido/Semana46/tim/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana46/Vivo/CDR/ --tipo ericsson_voz -s data/cdr_traduzido/Semana46/vivo/ericsson/ -n 8 \
&& uv run --python pypy3 src/teleparser/main.py data/cdr_bruto/Semana46/Claro/53524002349202519_12036747_GR04_GR04FI13_Of50_SMP_ERICSSON_140425 --tipo ericsson_voz -s data/cdr_traduzido/Semana46/claro/ericsson/ -n 8
 
 

 

