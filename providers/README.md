# providers/

Multi-provider eval scripts for [HumanEval](https://github.com/openai/human-eval). Each script calls a different LLM API and writes completions to a local folder for scoring.

## Providers

| File | Provider | Model | Output dir |
|---|---|---|---|
| `ai21.py` | AI21 Labs | j1-large | `ai21/` |
| `codegeex.py` | CodeGeeX | multilingual-adapt | `cg/` |
| `cohere.py` | Cohere | large | `cohere/` |
| `cushman.py` | OpenAI | code-davinci-002 | `cd/` |
| `yurts.py` | Yurts | 7B playground | `yurt/` |

## Setup

```bash
pip install -r requirements.txt
```

## Environment variables

Set the relevant vars before running a provider:

```bash
# AI21
export AI21_KEY="Bearer <token>"

# CodeGeeX
export CODEGEEX_APIKEY="<key>"
export CODEGEEX_APISECRET="<secret>"

# Cohere
export COHERE_KEY="<key>"

# OpenAI (cushman)
export OPENAI_KEY="<key>"

# Yurts — no key needed
```

## Run

```bash
# from repo root
python -m providers.ai21
python -m providers.codegeex
python -m providers.cohere
python -m providers.cushman
python -m providers.yurts
```

## Score

After generation, score with the upstream evaluator:

```bash
evaluate_functional_correctness <output_file>.jsonl
```

Sample runs are available in the [Releases](https://github.com/chirag127/human-eval/releases/tag/sample-runs) (AI21 + Yurts).
