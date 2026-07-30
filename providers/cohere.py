"""
Cohere provider — runs HumanEval against the Cohere large model.

Required env vars:
  COHERE_KEY — Cohere API key
"""

import os

from providers.helpers import get_samples, write_jsonl_in_folder

import cohere

NUM_SAMPLES_PER_TASK = 1


def generate_one_completion(prompt: str) -> str:
    """Generate one completion via Cohere large."""
    try:
        cohere_client = cohere.Client(os.environ["COHERE_KEY"])
        response = cohere_client.generate(
            model="large",
            prompt=prompt,
            max_tokens=100,
            temperature=0,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=[],
            return_likelihoods="NONE",
        )
        return response.generations[0].text
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        return "None"


def main() -> None:
    """Run HumanEval against Cohere large and write results to cohere/."""
    samples = get_samples(
        num_samples_per_task=NUM_SAMPLES_PER_TASK,
        _get_code_from_api=generate_one_completion,
    )
    write_jsonl_in_folder("cohere", samples)


if __name__ == "__main__":
    main()
