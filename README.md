# Playwright Python scalable framework

## Overview
Scalable Test Automation framework utilizing Python, Pytest, Poetry, and Playwright. Built with Page Object Model and Component Pattern.

## Build Setup
1. Clone the repository.
2. Ensure you have Python 3.10+ and Poetry installed.
3. Install dependencies: `poetry install`
4. Install Playwright engines: `poetry run playwright install chromium`
5. Setup pre-commit hooks: `poetry run pre-commit install`

## Run Tests
- Run all tests: `poetry run pytest`
- Run UI tests: `poetry run pytest -m ui`
- Run smoke tests: `poetry run pytest -m smoke`

## Project Structure
- `app/` - Application objects (Pages, Components)
- `config/` - Environment configs
- `data/` - Test data management
- `fixtures/` - Pytest fixtures (modular)
- `tests/` - The test cases
- `utils/` - Helpers (loggers, paths, assertions)

## Environment Variables
1. Copy `.env.example` to `.env`.
2. Select your environment (`ENV=local` or `ENV=dev`).

## Linters & Formatters
We use `ruff`, `black` and `pre-commit` to maintain quality.
Check code: `poetry run ruff check .`
Format code: `poetry run black .`
