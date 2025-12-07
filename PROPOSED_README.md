# LLMCode-Evaluation-Benchmark-Python-Framework

[![Build Status](https://img.shields.io/github/actions/workflow/user/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework/ci.yml?style=flat-square&logo=githubactions)](https://github.com/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework?style=flat-square&logo=codecov)](https://codecov.io/gh/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework)
[![Python Version](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Linting & Formatting](https://img.shields.io/badge/Ruff-✔-13294b?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/github/license/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework?style=flat-square&logo=github)](https://github.com/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework?style=flat-square&logo=github)](https://github.com/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework/stargazers)

**🚀 Automate the functional correctness benchmarking of Large Language Models (LLMs) on code generation tasks.** This robust Python framework ensures reliable and secure assessment by automating the evaluation of model-generated code against problem-solving datasets with detailed pass@k metrics.

---

## Architecture Diagram

mermaid
graph TD
    A[LLM Code Evaluator CLI] --> B{Core Evaluation Engine}
    B --> C[Dataset Loader]
    B --> D[LLM Code Generation Interface]
    B --> E[Code Execution & Verification]
    E --> F[Pass@k Metrics Calculator]
    D --> G[LLM APIs (e.g., Gemini)]
    C --> H[Problem Solving Datasets]
    E --> I[Secure Sandbox Environment]
    F --> J[Evaluation Reports]
    subgraph Core Components
        B
        C
        D
        E
        F
    end
    subgraph External Dependencies
        G
        H
        I
    end


---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [AI Agent Directives](#ai-agent-directives)
- [Development Standards](#development-standards)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Automated Benchmarking:** Effortlessly evaluate LLM code generation capabilities.
- **Functional Correctness:** Focus on verifying if generated code solves the intended problem.
- **Pass@k Metrics:** Comprehensive reporting using standard pass@k metrics.
- **Dataset Agnostic:** Designed to work with various problem-solving datasets.
- **Secure Execution:** Sandboxed environment for safe execution of generated code.
- **Extensible Interface:** Easily integrate new LLM providers and execution environments.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `uv` package manager

### Installation

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework.git
    cd LLMCode-Evaluation-Benchmark-Python-Framework
    

2.  **Install dependencies using `uv`:**
    bash
    uv install
    

---

## Usage

*Detailed command-line usage and examples will be provided in the CLI documentation.* For general execution:

bash
python -m llmcode_evaluator --dataset <path_to_dataset> --model <model_name> --output <output_directory>


---

<details>
  <summary>🤖 AI Agent Directives</summary>

## AGENT OPERATING DIRECTIVES (DECEMBER 2025 STANDARD)

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

### 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

### 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python) and apply the corresponding **Apex Toolchain**. This repository, `LLMCode-Evaluation-Benchmark-Python-Framework`, is a Python-based AI evaluation tool.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like dataset loading, LLM interaction, code execution, and reporting, while maintaining a unified deployment.
    *   **AI Integration:** Designed for deep integration with LLM APIs (e.g., Gemini, OpenAI). Prioritize modular design, clear API contracts, and robust error handling for all AI model interactions.
    *   **CLI Framework:** Uses `Click` for a powerful and intuitive command-line interface.

*   **TESTING FRAMEWORK (PYTHON):**
    *   **Unit & Integration Tests:** `Pytest` is the standard. Ensure comprehensive test coverage, adhering to the **Arrange-Act-Assert (AAA)** pattern.
    *   **Test Isolation:** Use `pytest-mock` for mocking external dependencies, ensuring deterministic test runs.
    *   **Fixtures:** Leverage `pytest` fixtures for setup and teardown, managing test resources efficiently.
    *   **Code Coverage:** Aim for **90%+ code coverage**, enforced by CI/CD pipelines. Use `coverage.py` integrated with `pytest`.

---

### 4. CODE QUALITY & DEVELOPMENT PRINCIPLES
*   **Linting & Formatting:** **Ruff** is mandated for lightning-fast linting and formatting. All code MUST pass Ruff checks without errors or warnings.
*   **Typing:** Implement strict type hints using Python's `typing` module. Use `mypy` for static type checking.
*   **SOLID Principles:** Adhere strictly to SOLID design principles for maintainable and scalable code.
*   **DRY (Don't Repeat Yourself):** Avoid code duplication through abstraction and modular design.
*   **YAGNI (You Ain't Gonna Need It):** Implement features only as required.
*   **Error Handling:** Implement robust, context-aware error handling. Use custom exception types where appropriate.

---

### 5. SECURITY MANDATES
*   **Dependency Scanning:** Regularly scan dependencies for vulnerabilities using `uv` or integrated CI/CD tools.
*   **Secure Execution:** Generated code MUST be executed within a hardened, isolated sandbox environment (e.g., Docker containers, `firejail`). Input sanitization is critical.
*   **Secret Management:** NEVER hardcode secrets. Use environment variables or secure secret management solutions.
*   **API Security:** When interacting with LLM APIs, use API keys securely and implement rate limiting.

---

### 6. CI/CD & AUTOMATION
*   **CI/CD Pipeline:** A GitHub Actions workflow (`ci.yml`) MUST be configured for automated building, linting, testing, and code coverage reporting on every push and pull request.
*   **Artifacts:** Build artifacts (e.g., Python wheels) should be generated and potentially published to a package index.

---

### 7. DOCUMENTATION & CONTRIBUTIONS
*   **README:** The `README.md` is the primary entry point. It MUST be comprehensive, clear, and up-to-date.
*   **CONTRIBUTING.md:** Clear guidelines for contributors.
*   **ISSUE_TEMPLATE & PR_TEMPLATE:** Standardized templates for issue reporting and pull requests.

---

### 8. ARCHIVAL PROTOCOL
*   **Retired Products:** Archived repositories are "Retired Products." Maintain professional, descriptive metadata (Name, Description, Topics) and ensure essential documentation (`README`, `LICENSE`) remains accessible and accurate. The code itself should be versioned and immutable.

---

### 9. APEX NAMING CONVENTION (STAR VELOCITY ENGINE)
*   **Formula:** `<Product-Name>-<Primary-Function>-<Platform>-<Type>`
*   **Format:** `Title-Case-With-Hyphens`
*   **Rules:** 3-10 words, high-volume keywords, NO numbers, NO emojis, NO underscores, NO generic words without qualifiers.

---

### 10. DYNAMIC URL & BADGE PROTOCOL
*   **Base URL:** `https://github.com/chirag127/<New-Repo-Name>`
*   **Badge Consistency:** All badges MUST use the dynamic Base URL. Never reference old repository names.

---

### 11. STANDARD 11 COMPLIANCE
*   Every repository MUST adhere to the 11 essential files for professional archival and operation.

</details>

---

## Development Standards

- **Principles:** Adherence to SOLID, DRY, and YAGNI principles.
- **Linting & Formatting:** Enforced by **Ruff**. All code must conform.
- **Type Checking:** Strict type hints using Python's `typing` module, checked with `mypy`.
- **Testing:** Comprehensive unit and integration tests using `Pytest`, aiming for **90%+ code coverage**.
- **Error Handling:** Robust and context-aware error management.

---

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](https://github.com/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework/blob/main/CONTRIBUTING.md) file for detailed guidelines.

---

## License

This project is licensed under the [CC BY-NC 4.0](https://github.com/chirag127/LLMCode-Evaluation-Benchmark-Python-Framework/blob/main/LICENSE) license.
