# human-eval

[![GitHub Stars](https://img.shields.io/github/stars/chirag127/human-eval?style=flat-square)](https://github.com/chirag127/human-eval/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square)](https://www.python.org/)

Fork of [openai/human-eval](https://github.com/openai/human-eval) extended with multi-provider LLM eval scripts.

The upstream `human_eval/` package (data loading, sandboxed execution, pass@k evaluation) is kept as-is. The `providers/` directory adds eval harnesses for AI21, CodeGeeX, Cohere, OpenAI Cushman/Davinci, and Yurts.

---

## Providers supported

| Provider | Model | Script |
|---|---|---|
| AI21 Labs | j1-large | `providers/ai21.py` |
| CodeGeeX | multilingual-adapt | `providers/codegeex.py` |
| Cohere | large | `providers/cohere.py` |
| OpenAI | code-davinci-002 | `providers/cushman.py` |
| Yurts | 7B playground | `providers/yurts.py` |

---

## Setup

```bash
git clone https://github.com/chirag127/human-eval.git
cd human-eval
pip install -r requirements.txt
pip install -e .
```

## Running an eval

Set provider env vars (see [`providers/README.md`](providers/README.md)), then:

```bash
python -m providers.ai21        # or any other provider
```

Output `.jsonl` files land in a local folder (`ai21/`, `cg/`, etc.).

## Scoring (pass@k)

```bash
evaluate_functional_correctness <path/to/output.jsonl>
```

pass@k is the probability that at least one of k generated completions passes all test cases for a problem. The upstream evaluator computes pass@1, pass@10, pass@100.

## Sample runs

Pre-generated outputs for AI21 j1-large and Yurts 7B are in [Releases → sample-runs](https://github.com/chirag127/human-eval/releases/tag/sample-runs).

---

## Upstream credit

`human_eval/` package and `data/` are from [openai/human-eval](https://github.com/openai/human-eval), MIT licensed. This fork adds multi-provider scripts only.

## License

MIT — see [LICENSE](LICENSE).
