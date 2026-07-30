"""
CodeGeeX provider — runs HumanEval against the CodeGeeX multilingual model.

Required env vars:
  CODEGEEX_APIKEY    — CodeGeeX API key
  CODEGEEX_APISECRET — CodeGeeX API secret
"""

import os

import requests
from providers.helpers import get_samples, write_jsonl_in_folder

NUM_SAMPLES_PER_TASK = 102


def codegeex_api(prompt: str) -> str:
    """Generate one completion via the CodeGeeX multilingual API."""
    payload = {
        "prompt": prompt,
        "n": 1,
        "apikey": os.environ["CODEGEEX_APIKEY"],
        "apisecret": os.environ["CODEGEEX_APISECRET"],
        "temperature": 0.8,
        "top_p": 1,
        "top_k": 0,
    }
    response = requests.post(
        "https://tianqi.aminer.cn/api/v2/multilingual_code_generate_adapt",
        json=payload,
        timeout=30,
    )
    response = response.json()
    code = response["result"]["output"]["code"][0]
    print(code)
    return code


def main() -> None:
    """Run HumanEval against CodeGeeX and write results to cg/."""
    samples = get_samples(
        num_samples_per_task=NUM_SAMPLES_PER_TASK, _get_code_from_api=codegeex_api
    )
    write_jsonl_in_folder("cg", samples)


if __name__ == "__main__":
    main()
