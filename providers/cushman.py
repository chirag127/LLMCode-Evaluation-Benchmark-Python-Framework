"""
OpenAI Cushman/Davinci provider — runs HumanEval against code-davinci-002.

Required env vars:
  OPENAI_KEY — OpenAI API key
"""

import os
from time import sleep

import openai
from providers.helpers import get_samples, write_jsonl_in_folder

NUM_SAMPLES_PER_TASK = 1


def generate(prompt: str) -> str:
    """Generate one completion via OpenAI code-davinci-002."""
    try:
        openai.api_key = os.environ["OPENAI_KEY"]
        sleep(3)
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=prompt,
            temperature=0.2,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\nclass", "\ndef"],
        )
        sleep(20)
        code = response.choices[0].text
        print("".join([prompt, code]))
        return code
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        return ""


def main() -> None:
    """Run HumanEval against OpenAI code-davinci-002 and write results to cd/."""
    samples = get_samples(
        num_samples_per_task=NUM_SAMPLES_PER_TASK, _get_code_from_api=generate
    )
    write_jsonl_in_folder("cd", samples)


if __name__ == "__main__":
    main()
