"""
Yurts provider — runs HumanEval against a self-hosted Yurts 7B model endpoint.

No API key required; hits the public playground endpoint directly.
"""

import requests
from providers.helpers import get_samples, write_jsonl_in_folder

NUM_SAMPLES_PER_TASK = 102


def generate_one_completion(prompt: str) -> str:
    """Generate one completion via the Yurts 7B playground endpoint."""
    response = requests.post(
        "https://lb.yurts.ai/models/7b36cc5a-d6e9-4241-aee8-b299fc1280c7-12/prediction",
        headers={
            "authority": "lb.yurts.ai",
            "accept": "application/json, text/plain, */*, application/json",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://playground.yurts.ai",
            "referer": "https://playground.yurts.ai/",
            "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetcher-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        },
        json={"text": prompt},
    )
    response = response.json()
    code = response["text"].replace(prompt, "", 1)
    print(code)
    return code


def main() -> None:
    """Run HumanEval against Yurts 7B and write results to yurt/."""
    samples = get_samples(
        num_samples_per_task=NUM_SAMPLES_PER_TASK,
        _get_code_from_api=generate_one_completion,
    )
    write_jsonl_in_folder("yurt", samples)


if __name__ == "__main__":
    main()
