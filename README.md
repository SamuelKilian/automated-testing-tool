# Automated Testing Tool

A Python project focused on automated functional testing, input validation, and reliable software behavior using `pytest`.

## Overview

This project demonstrates how automated tests can be used to verify expected software behavior, detect errors, and improve software reliability.

The initial implementation focuses on a simple average-calculation function and tests its behavior under normal conditions, edge cases, and invalid inputs.

**Project status:** In development.

## Features

- Automated functional tests using `pytest`
- Verification of expected results with assertions
- Testing of positive and negative numbers
- Edge-case testing with a single input value
- Validation of invalid inputs using exception handling
- Clear test results directly in the terminal

## Technologies

- **Python** — implementation of the function under test
- **pytest** — automated test execution and assertions
- **Git** — version control

## Project Structure

```text
automated-testing-tool/
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/SamuelKilian/automated-testing-tool.git
cd automated-testing-tool
```

Create and activate a virtual environment.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Running the Tests

Execute the test suite from the project root:

```bash
python -m pytest -v
```

The terminal displays the result of each test, including whether it passed or failed.

## Test Scenarios

| Scenario | Expected Behavior |
|---|---|
| Positive numbers | Returns the correct average |
| Negative numbers | Returns the correct average |
| Single input value | Returns that value |
| Empty list | Raises a `ValueError` |

## Future Improvements

- Expand test coverage with additional edge cases and invalid inputs
- Improve test organization and reusability
- Generate more detailed test reports
- Integrate automated test execution into a CI pipeline using GitHub Actions
- Explore testing strategies for more complex software components

## Learning Objectives

- Understand the principles of automated software testing
- Write and organize test cases with `pytest`
- Validate expected behavior and error handling
- Use test results to identify regressions and improve software reliability

---

*This project is being developed as a practical exploration of automated testing and software quality assurance.*
