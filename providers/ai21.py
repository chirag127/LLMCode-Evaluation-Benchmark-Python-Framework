"""
AI21 Labs provider — runs HumanEval against the j1-large model.

Required env vars:
  AI21_KEY  — "Bearer <token>" authorization header value
"""

import os

import requests
from providers.helpers import get_samples, write_jsonl_in_folder

NUM_SAMPLES_PER_TASK = 11


def generate_one_completion(prompt: str) -> str:
    """Generate one completion via AI21 j1-large."""
    ai21_key = os.environ["AI21_KEY"]
    response = requests.post(
        "https://api.ai21.com/studio/v1/j1-large/complete",
        timeout=60,
        headers={
            "authority": "api.ai21.com",
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "authorization": ai21_key,
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://studio.ai21.com",
            "referer": "https://studio.ai21.com/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "x-requested-with": "XMLHttpRequest",
        },
        json={
            "prompt": prompt,
            "model": "j1-large",
            "temperature": 0.2,
            "topP": 1,
            "maxTokens": 100,
            "numStopSequences": 1,
            "stopSequences": ["\ndef ", "\nclass ", "\n\n#", "\n\n\n\n"],
            "stream": False,
            "frequencyPenalty": {
                "scale": 0.01,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True,
            },
            "presencePenalty": {
                "scale": 0.01,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True,
            },
            "countPenalty": {
                "scale": 0.01,
                "applyToWhitespaces": True,
                "applyToPunctuations": True,
                "applyToNumbers": True,
                "applyToStopwords": True,
                "applyToEmojis": True,
            },
        },
    )
    response = response.json()
    text = response["completions"][0]["data"]["text"]
    print(text)
    print("-" * 84)
    return text


def main() -> None:
    """Run HumanEval against AI21 j1-large and write results to ai21/."""
    for _ in range(10):
        samples = get_samples(
            num_samples_per_task=NUM_SAMPLES_PER_TASK,
            _get_code_from_api=generate_one_completion,
        )
        write_jsonl_in_folder("ai21", samples)


if __name__ == "__main__":
    main()
