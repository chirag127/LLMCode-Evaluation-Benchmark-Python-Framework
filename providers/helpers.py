"""
Shared helpers for all provider eval scripts.

Used by every provider to load HumanEval problems, call an API, and write output.
"""

import os
import random

from human_eval.data import read_problems, write_jsonl


def get_samples(num_samples_per_task: int, _get_code_from_api) -> list:
    """Return list of {task_id, completion} dicts for all HumanEval problems."""
    problems = read_problems()
    return [
        dict(
            task_id=task_id,
            completion=_generate(problems[task_id]["prompt"], _get_code_from_api),
        )
        for task_id in problems
        for _ in range(num_samples_per_task)
    ]


def _generate(prompt: str, _get_code_from_api) -> str:
    try:
        return _get_code_from_api(prompt)
    except Exception as error:  # pylint: disable=broad-except
        print(error)
        return ""


def write_jsonl_in_folder(folder_name: str, samples: list) -> None:
    """Write samples to a randomly-named .jsonl inside folder_name/."""
    file_name = str(random.random()).replace(".", "_") + ".jsonl"
    os.makedirs(folder_name, exist_ok=True)
    write_jsonl(os.path.join(folder_name, file_name), samples)
