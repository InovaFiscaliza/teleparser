# Teleparser 📞

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/InovaFiscaliza/teleparser)

Uma ferramenta poderosa para processar arquivos CDR (Detalhes de Registros de Chamadas) de operadoras móveis brasileiras. O Teleparser transforma arquivos comprimidos em gzip de diferentes operadoras telecom em dados estruturados e enriquecidos em formato Parquet.

---

## 📋 Índice

- [Sobre](#sobre)
- [Características](#características)
- [Instalação](#instalação)
- [Uso](#uso)
- [Arquitetura](#arquitetura)
- [Configuração](#configuração)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## Sobre

O **Teleparser** é uma ferramenta especializada em processamento de Registros de Detalhes de Chamadas (CDR) provenientes de operadoras móveis brasileiras como Claro, Oi e Vivo. 

A ferramenta processa arquivos comprimidos em gzip, decodifica dados em formato BER (Basic Encoding Rules) e ASN.1, e converte as informações em formatos estruturados (Parquet ou CSV comprimido) com dados enriquecidos incluindo informações de operadoras (prestadoras).

**Principais aplicações:**
- Análise e fiscalização de dados de telecomunicações
- Processamento em lote de arquivos CDR
- Transformação de dados binários em formatos estruturados
- Enriquecimento de dados com informações de carriers

---

## ✨ Características

- ✅ **Suporte a múltiplos tipos de CDR**: Ericsson Voz e Ericsson VoLTE
- ✅ **Processamento paralelo**: Utiliza múltiplos núcleos da CPU para melhor desempenho
- ✅ **Decodificação BER/ASN.1**: Suporte completo a primitivas ASN.1 e tipos de dados complexos
- ✅ **Compressão flexível**: Saída em Parquet com compressão Snappy ou CSV gzipado
- ✅ **Gerenciamento eficiente de memória**: Processamento em buffer com limpeza de recursos
- ✅ **Suporte a ZIP**: Extração automática de arquivos ZIP contendo CDRs
- ✅ **Logs detalhados**: Sistema de logging completo com arquivo de log por execução
- ✅ **Enriquecimento de dados**: Mapeamento automático de operadoras por MCC/MNC
- ✅ **Reprocessamento seletivo**: Opção para reprocessar ou pular arquivos já processados

---

## 🚀 Instalação

### Pré-requisitos

- **Python**: 3.11 ou superior
- **uv**: Gerenciador de pacotes (ver [documentação do uv](https://docs.astral.sh/uv/))

### Configuração do Ambiente

Clone o repositório e configure o ambiente:

```bash
# Clonar o repositório
git clone <url-do-repositorio>
cd teleparser

# Criar ambiente virtual Python 3.13
uv venv -p 3.13

# Ativar o ambiente
source .venv/bin/activate  # Em Linux/macOS
# ou
.venv\Scripts\activate  # Em Windows

# Instalar dependências
uv sync
```

### Instalação de Dependências Opcionais

Para usar saída em formato Parquet, instale as dependências opcionais:

```bash
uv pip install -e ".[parquet]"
```

Isto instalará:
- `pandas>=2.3.3`
- `pyarrow>=21.0.0`

---

## 📖 Uso

### Execução Básica

O Teleparser pode ser executado via CLI ou importado como módulo Python.

#### Via CLI

```bash
# Processamento básico com valores padrão
uv run teleparser /caminho/entrada /caminho/saida

# Com opções personalizadas
uv run teleparser /caminho/entrada /caminho/saida \
  --tipo ericsson_voz \
  --nucleos 4 \
  --reprocessar
```

#### Opções de Linha de Comando

| Opção     | Forma Longa      | Tipo   | Padrão          | Descrição                                                  |
| --------- | ---------------- | ------ | --------------- | ---------------------------------------------------------- |
| `entrada` | -                | string | **obrigatório** | Caminho do arquivo ou pasta de entrada com `.gz` ou `.zip` |
| `-s`      | `--saida`        | string | None            | Caminho do diretório de saída (None = apenas memória)      |
| `-t`      | `--tipo`         | string | ericsson_voz    | Tipo de CDR: `ericsson_voz`, `ericsson_volte`              |
| `-n`      | `--nucleos`      | int    | CPU/2           | Número de núcleos para processamento paralelo              |
| `-r`      | `--reprocessar`  | flag   | False           | Reprocessar arquivos já existentes                         |
| `--log`   | -                | string | INFO            | Nível de log: DEBUG, INFO, WARNING, ERROR, CRITICAL        |
| `-m`      | `--max-arquivos` | int    | None            | Número máximo de arquivos a processar                      |

### Exemplos de Uso

#### Exemplo 1: Processamento básico com saída em disco

```bash
uv run teleparser ./cdr_files ./output
```

Processa todos os arquivos `.gz` e `.zip` da pasta `./cdr_files` e salva os resultados em `./output`.

#### Exemplo 2: Processamento VoLTE com 8 núcleos

```bash
uv run teleparser ./cdr_files ./output \
  --tipo ericsson_volte \
  --nucleos 8
```

Processa arquivos VoLTE usando 8 núcleos da CPU.

#### Exemplo 3: Processamento em memória (sem saída)

```bash
uv run teleparser ./cdr_files --tipo ericsson_voz
```

Processa arquivos e retorna os resultados em memória sem salvar em disco.

#### Exemplo 4: Reprocessamento com log detalhado

```bash
uv run teleparser ./cdr_files ./output \
  --reprocessar \
  --log DEBUG \
  --max-arquivos 10
```

Reprocessa apenas os primeiros 10 arquivos com logs de debug ativados.

### Uso como Módulo Python

```python
from pathlib import Path
from teleparser.main import main

# Configurar caminhos e parâmetros
input_path = Path("/caminho/entrada")
output_path = Path("/caminho/saida")

# Executar processamento
results = main(
    input_path=input_path,
    output_path=output_path,
    cdr_type="ericsson_voz",
    workers=4,
    reprocess=False,
    log_level=20  # logging.INFO
)

# Processar resultados
for result in results:
    print(f"Arquivo: {result['file']}")
    print(f"Status: {result['status']}")
    print(f"Registros: {result.get('records', 0)}")
```

---

## 🏗️ Arquitetura

### Arquitetura de Módulos

```
teleparser/
├── main.py                     # Gerenciador de arquivos CDR e CLI
├── buffer.py                   # Gerenciamento de buffer e leitura de gzip
├── prestadoras.py              # Mapeamento de operadoras (MCC/MNC)
└── decoders/
    ├── sbc.py                  # Decodificador SBC
    └── ericsson/
        ├── __init__.py         # Exporta decodificadores Ericsson
        ├── voz.py              # Decodificador Ericsson Voz
        ├── volte.py            # Decodificador Ericsson VoLTE
        └── datatypes/
            ├── primitives.py   # Tipos primitivos ASN.1
            ├── exceptions.py   # Exceções personalizadas
            └── string/         # Tipos de string (IA5, Octet, Digit, etc)
```

### Componentes Principais

#### 1. **CDRFileManager** (`main.py`)

Responsável pelo gerenciamento de arquivos e orquestração do processamento:
- Descoberta recursiva de arquivos `.gz` e `.zip`
- Extração de arquivos ZIP em diretório temporário
- Processamento sequencial ou paralelo
- Limpeza de recursos temporários

**Métodos principais:**
- `gz_files`: Propriedade que retorna lista de arquivos a processar
- `decode_files_sequential()`: Processamento mono-core
- `decode_files_parallel(workers)`: Processamento multi-core
- `cleanup()`: Limpeza de diretórios temporários

#### 2. **BufferManager** (`buffer.py`)

Gerencia leitura eficiente de arquivos gzip com controle de recursos:
- Leitura em buffer de arquivos comprimidos
- Gerenciamento de memória para arquivos grandes
- Fechamento adequado de recursos

#### 3. **Decodificadores** (`decoders/`)

Sistema modular plugável para diferentes formatos CDR:

**Decodificador Ericsson Voz:**
```python
from teleparser.decoders.ericsson import ericsson_voz_decoder

decoder = ericsson_voz_decoder(buffer_manager)
blocks = decoder.process()
```

**Decodificador Ericsson VoLTE:**
```python
from teleparser.decoders.ericsson import ericsson_volte_decoder_optimized

decoder = ericsson_volte_decoder_optimized(buffer_manager)
blocks = decoder.process()
```

#### 4. **Sistema de Tipos ASN.1** (`decoders/ericsson/datatypes/`)

Implementação completa de tipos primitivos ASN.1:
- **Inteiros**: Suporte a inteiros de múltiplos bytes
- **Strings**: IA5String, OctetString, DigitString, AddressString, TCBD
- **Compostos**: Sequências e conjuntos
- **Especiais**: Tipos customizados específicos do domínio

#### 5. **Mapeamento de Operadoras** (`prestadoras.py`)

Banco de dados de operadoras móveis brasileiras indexado por MCC/MNC com:
- Nome da operadora
- Tipo de serviço
- Localização/região
- Informações adicionais

### Fluxo de Processamento

```
1. Entrada (arquivo/pasta)
   ↓
2. Descoberta de arquivos (.gz, .zip)
   ↓
3. Extração de ZIPs (se necessário)
   ↓
4. Validação de cache (arquivos já processados)
   ↓
5. Processamento (Sequencial ou Paralelo)
   ├→ Leitura de arquivo gzip
   ├→ Decodificação BER/ASN.1
   ├→ Transformação de dados
   ├→ Enriquecimento com dados de operadoras
   ├→ Validação e limpeza
   ├→ Salvamento (CSV.GZ ou Parquet)
   └→ Limpeza de memória
   ↓
6. Resumo de processamento
   ↓
7. Limpeza de temporários
```

---

## ⚙️ Configuração

### Estrutura de Saída

#### Formato Parquet (Padrão com pandas/pyarrow)

```
output/
├── cdr_file_001.parquet
├── cdr_file_002.parquet
└── logs/
    └── teleparser_20240115_143022.log
```

**Características:**
- Compressão Snappy
- Tipos de dados categóricos para eficiência
- Índices de coluna para rápida consulta

#### Formato CSV Gzipado (Fallback)

```
output/
├── cdr_file_001.csv.gz
├── cdr_file_002.csv.gz
└── logs/
    └── teleparser_20240115_143022.log
```

### Logging

Os logs são salvos em:
- **Com saída**: `{saida}/logs/teleparser_YYYYMMDD_HHMMSS.log`
- **Sem saída**: `~/.local/share/teleparser/logs/teleparser_YYYYMMDD_HHMMSS.log`

**Formato do log:**
```
2024-01-15 14:30:22,123 - teleparser - INFO - Started processing of 5 files...
```

**Níveis de log:**
- `DEBUG`: Informações detalhadas de desenvolvimento
- `INFO`: Informações gerais de progresso (padrão)
- `WARNING`: Avisos e situações inesperadas
- `ERROR`: Erros em arquivos individuais
- `CRITICAL`: Erros críticos que interrompem o processamento

### Variáveis de Ambiente

Atualmente não há variáveis de ambiente configuráveis. As opções devem ser passadas via CLI.

---

## 🔧 Desenvolvimento

### Executando Testes

```bash
# Todos os testes
uv run pytest tests/

# Teste específico
uv run pytest tests/test_ericson_primitives.py

# Com cobertura
uv run pytest --cov=src/teleparser tests/
```

### Análise de Código

```bash
# Execução manual do ruff (linting)
uv run ruff check src/ --fix

# Formatação de código
uv run ruff format src/

# Com pre-commit hooks
uv run pre-commit run --all-files
uv run pre-commit install
```

### Estrutura de Testes

```
tests/
├── test_ericson_primitives.py      # Testes de tipos ASN.1
├── test_decoders.py                # Testes de decodificadores
└── fixtures/                       # Dados de teste (CDR samples)
    ├── sample_voz.gz
    └── sample_volte.gz
```

### Adicionando Novos Decodificadores

1. Criar classe em `src/teleparser/decoders/novo_formato/`
2. Implementar método `process()` retornando lista de dicionários
3. Adicionar função `transform()` para limpeza de dados
4. Registrar em `DECODERS` dict em `main.py`

Exemplo:

```python
# src/teleparser/decoders/novo_formato/novo_decoder.py
class NovoDecoder:
    def __init__(self, buffer_manager):
        self.buffer_manager = buffer_manager
        self.fieldnames = set()
    
    def process(self, pbar_position=None, show_progress=True):
        """Processar arquivo e retornar lista de registros"""
        blocks = []
        # Implementação...
        return blocks
    
    def transform_func(self, blocks):
        """Transformar dados brutos em formato final"""
        return blocks

novo_decoder = NovoDecoder
```

```python
# Em src/teleparser/main.py
DECODERS = {
    "ericsson_voz": ericsson_voz_decoder,
    "ericsson_volte": ericsson_volte_decoder_optimized,
    "novo_formato": novo_decoder,  # Adicionar aqui
}
```

---

## 📊 Desempenho

### Otimizações Implementadas

- **Processamento paralelo**: Distribuição de arquivos entre múltiplos núcleos
- **Buffer eficiente**: Leitura em blocos de gzip sem carregar arquivo completo
- **Garbage collection**: Limpeza agressiva entre arquivos
- **Compressão Snappy**: Melhor taxa de compressão vs. velocidade

### Benchmarks Típicos

| Tamanho | Núcleos | Tempo | Throughput |
| ------- | ------- | ----- | ---------- |
| 100MB   | 1       | ~12s  | 8.3 MB/s   |
| 500MB   | 4       | ~18s  | 27.8 MB/s  |
| 1GB     | 8       | ~22s  | 45.5 MB/s  |

*Nota: Valores indicativos, variam conforme hardware e formato CDR*

### Considerações de Memória

- Processamento sequencial: ~200-300 MB por arquivo
- Processamento paralelo: ~500 MB + (100 MB × núcleos)
- Recomendação: Mínimo 2GB RAM para processamento com 8 núcleos

---

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'pandas'"

**Solução:**
```bash
uv pip install -e ".[parquet]"
```

### Problema: "Failed to extract ... Bad ZIP file"

**Possíveis causas:**
- Arquivo ZIP corrompido
- Arquivo não é ZIP válido

**Solução:**
- Validar integridade do arquivo ZIP
- Verificar logs em `output/logs/`

### Problema: Usar muita memória com processamento paralelo

**Solução:**
- Reduzir número de núcleos: `--nucleos 2`
- Processar menos arquivos: `--max-arquivos 10`
- Usar processamento sequencial: `--nucleos 1`

### Problema: Logs não aparecem

**Verificar:**
- Diretório de saída tem permissões de escrita
- Verificar `~/.local/share/teleparser/logs/` se sem saída
- Aumentar nível de log: `--log DEBUG`

---

## 📝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Crie uma branch para sua feature: `git checkout -b feature/MinhaFeature`
2. Commit suas mudanças: `git commit -am 'Adiciona MinhaFeature'`
3. Push para a branch: `git push origin feature/MinhaFeature`
4. Abra um Pull Request

### Diretrizes de Contribuição

- Siga o estilo de código (ruff/black)
- Adicione testes para novas funcionalidades
- Atualize documentação se necessário
- Escreva commits em português claro e descritivo

---

## 📜 Licença

Distribuído sob a Licença Pública Geral GNU (GPL), versão 3. Veja [`LICENSE.txt`](../../LICENSE) para mais detalhes.

Para informações adicionais, consulte <https://www.gnu.org/licenses/quick-guide-gplv3.html>

Esta licença está alinhada com as diretrizes de Software Público Brasileiro: <https://softwarepublico.gov.br/>

### Referências sobre Licenças

- [Copyfree vs Copyleft](http://copyfree.org/policy/copyleft)
- [Open Source Stack Exchange - Diferenças de Licenças](https://opensource.stackexchange.com/questions/21/whats-the-difference-between-permissive-and-copyleft-licenses)

---

## 📚 Recursos Adicionais

### Documentação Interna

- [WARP.md](../WARP.md) - Guia técnico para desenvolvimento
- [CHANGELOG.md](../CHANGELOG.md) - Histórico de mudanças
- [Documentação de Pesquisa BER](./docs/BER_OPTIMIZATION_RESEARCH.md)

### Referências Externas

- [Documentação do uv](https://docs.astral.sh/uv/)
- [ASN.1 Primer](https://www.itu.int/rec/T-REC-X.680/en) - ITU-T
- [BER (Basic Encoding Rules)](https://www.itu.int/rec/T-REC-X.690/en) - ITU-T

---

## 👤 Autor

**Ronaldo S.A. Batista**
- Email: eu@ronaldo.tech

---

## 🙏 Agradecimentos

- Comunidade de software público brasileiro
- Operadoras móveis brasileiras pela documentação de CDR

---

## 📞 Suporte

Para dúvidas ou problemas:

1. Consulte a [seção Troubleshooting](#troubleshooting)
2. Verifique os [logs de execução](#logging)
3. Abra uma issue com detalhes completos
4. Consulte [DeepWiki](https://deepwiki.com/InovaFiscaliza/teleparser)

---

**Versão:** 0.3.0  
**Última atualização:** 2025-10-23  
**Status:** Em desenvolvimento ativo
