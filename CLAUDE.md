# Guidelines for AI Coding Assistants (Antigravity & Claude Code)

Follow these strict rules when contributing to `playwright-automation`:

## Architecture
- Use Page Object Model (pages/ folder) alongside Component Pattern (components/ folder) for reusable parts.
- Flows should be implemented outside of page objects to keep actions atomic.

## Anti-patterns (STRICT prohibitions)
- **no assertions in page objects**: Page objects should only return data or states. Tests assert the values.
- **no business logic in BasePage**: `BasePage` is strictly a wrapper around Playwright primitives (`fill`, `click`, `wait_for`).
- **no time.sleep()**: ALWAYS use explicit waits or Playwright's auto-waiting mechanism.
- **no locators in tests**: Locators (`page.locator(...)`) belong ONLY in page objects or components.
- **no duplicated setup**: Move setups to `fixtures/` or `conftest.py`.
- **no uncontrolled random**: Use predictable deterministic random or explicitly configured data factories.

## Implementation details
- Playwright's `fill()` method should always be used over `type()`.
- Use specific pytest markers for every test module/class/function (`@pytest.mark.ui`, `@pytest.mark.smoke`, etc.).
- Maintain `__init__.py` recursively in packages.
