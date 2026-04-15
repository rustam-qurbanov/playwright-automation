# 🎭 Playwright Python Scalable Framework

> Production-ready UI/API test automation framework built with Python, Pytest, and Playwright.
> Designed with a strict focus on scalability, clean architecture, and test stability.

---

## 🎯 Why This Framework & Philosophy

This framework is designed to:
* Eliminate flaky tests by relying entirely on Playwright's auto-waiting.
* Enforce clean separation of concerns between tests, flows, pages, and fixtures.
* Ensure tests read like user behavior, not implementation details.
* Support fast execution through API-based setups.
* Provide a scalable architecture that grows from simple scenarios to full enterprise regression coverage.

---

## 🌟 Key Features

* **Strict Architecture:** Strict separation of tests, flows, and page objects.
* **Zero Locators in Tests:** Tests read like plain English; all DOM interaction is encapsulated.
* **High Stability:** Complete reliance on Playwright's auto-waiting. No `time.sleep()`.
* **API + UI:** Support for dual-layer testing (handling setups via API to speed up UI tests).
* **Code Quality:** Formatted and linted strictly via `ruff`, `black` and `pre-commit`.

---

## 🧾 Example Test

Tests inside this framework are incredibly readable and focus purely on business logic:

```python
def test_user_can_checkout_item(auth_flow, cart_flow, inventory_page):
    auth_flow.login_as_standard_user()
    inventory_page.add_random_item_to_cart()
    cart_flow.complete_checkout()

    assert inventory_page.is_checkout_successful()
```

---

## 🏗️ Project Structure

The repository follows a clean, modular structure:

```text
├── app/
│   ├── pages/         # Page Objects (UI interactions)
│   ├── components/    # Reusable UI fragments (Headers, Modals, Tables)
│   └── api/           # API clients for fast setups/assertions
├── flows/             # Business workflows combining multiple pages
├── fixtures/          # Pytest fixtures (setup/teardown)
├── tests/             # High-level test logic (Arrange -> Act -> Assert)
├── data/              # Centralized test data and builders
├── models/            # Typed request/response models (Pydantic/Dataclasses)
├── config/            # Environment configurations
├── utils/             # Minimal helpers (loggers, paths, strings)
└── artifacts/         # Screenshots, traces, and execution videos
```

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.10+**
* **Poetry** (Environment and dependency manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/rustam-qurbanov/playwright-automation.git
   cd playwright-automation
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Install Playwright browsers:**
   ```bash
   poetry run playwright install chromium
   # or install all browsers: poetry run playwright install
   ```

4. **Install Pre-commit hooks:**
   ```bash
   poetry run pre-commit install
   ```

5. **Environment Configuration:**
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

---

## 🧪 Running Tests

The framework uses Pytest. All tests can be executed via `poetry run pytest`.

**Basic Test Executions:**
```bash
# Run all tests
poetry run pytest

# Run tests with specific markers
poetry run pytest -m ui
poetry run pytest -m smoke

# Run a specific test file
poetry run pytest tests/login/test_login.py
```

**Playwright Debugging & Visuals:**
```bash
# Run in headed mode (UI visible)
poetry run pytest --headed

# Run with Playwright UI mode (Interactive time-travel debugger)
poetry run pytest --ui

# Record traces for failed tests
poetry run pytest --tracing=retain-on-failure

# Generate a Playwright HTML report
poetry run pytest --html=report.html
```

---

## 🛡️ Coding Standards & Principles

1. **Arrange -> Act -> Assert:** All tests must strictly follow this pattern.
2. **No Assertions in Pages:** Page objects only interact and return data. Asserts belong in `tests/`.
3. **No Locators in Tests:** Selectors and locators stay in `app/pages` and `app/components`.
4. **Deterministic Waits:** Never use `time.sleep()`. Rely on Playwright's web-first assertions and auto-waiting.

---

## 🧑‍💻 Code Quality

This project enforces strict code quality formatting.
Before committing, pre-commit hooks will automatically format your code.

```bash
# Run linter manually
poetry run ruff check .

# Run formatter manually
poetry run ruff format .
# or if using black: poetry run black .
```

---

## 📌 Scope & Future Roadmap

**Current Scope:**
- UI automation (Playwright)
- API-assisted test setup
- Scalable AQA architecture

**Future Integrations:**
- Appium (Mobile Automation)
- CI/CD Pipelines (GitHub Actions / GitLab CI)
- Advanced visual reporting (Allure)
