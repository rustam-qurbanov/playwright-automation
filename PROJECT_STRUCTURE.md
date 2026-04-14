# Project Structure

## Обзор проекта

- **Домен:** E-commerce платформа (Sauce Demo)
- **Что тестируем:** UI (Playwright, sync API) + API (REST)
- **Стек:** Python 3.12+ / Pytest / Playwright / Poetry / Ruff
- **Цель:** production-ready фреймворк автоматизации

---

## Полная структура

```
playwright-automation/
│
├── .claude/                               # Настройки ИИ-ассистента
├── CLAUDE.md                              # Контракт: архитектура, правила, чеклисты
├── CLAUDE_EXAMPLES.md                     # Примеры идеального кода по стандартам проекта
├── conftest.py                            # Корневой conftest — загружает .env, импортирует фикстуры
├── pytest.ini                             # Маркеры, флаги, пути к тестам
├── pyproject.toml                         # Poetry: зависимости + настройки ruff
├── poetry.lock                            # Фиксированные версии зависимостей
├── Makefile                               # Шорткаты для частых команд (см. ниже)
├── .env                                   # Секреты — НЕ коммитится (в .gitignore)
├── .env.example                           # Шаблон переменных окружения
├── .pre-commit-config.yaml                # Хуки: ruff format + ruff check
├── .gitignore
├── README.md
│
├── artifacts/                             # Генерируется при прогоне — НЕ коммитится
│   ├── screenshots/                       # Скриншоты при падении тестов
│   ├── traces/                            # Playwright traces
│   └── videos/                            # Видеозаписи тестов
│
├── config/
│   ├── __init__.py
│   ├── settings.py                        # Читает среду из ENV → загружает нужный JSON
│   ├── constants.py                       # Глобальные константы: роли, статусы, лимиты
│   └── environments/
│       ├── local.json                     # timeout: 30s, headless: false
│       └── dev.json                       # timeout: 60s, headless: true
│
├── app/
│   ├── __init__.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py                   # Атомарные обёртки: click, fill, hover, get_text,
│   │   │                                  # is_visible, is_hidden, wait_for, navigate
│   │   ├── login_page.py                  # Локаторы + действия: login(), get_error_message()
│   │   └── inventory_page.py              # Локаторы + действия: get_title(), get_item_count()
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── base_component.py              # Базовый класс: принимает page + root_locator
│   │   └── header.py                      # Шапка: cart_count(), open_menu(), logout()
│   │
│   └── api/
│       ├── __init__.py
│       ├── base_api.py                    # HTTP-обёртка: get, post, put, delete + логирование
│       └── auth_api.py                    # POST /login, возвращает AuthResponse из models/
│
├── flows/
│   ├── __init__.py
│   └── auth_flow.py                       # open → login → return InventoryPage
│
├── fixtures/
│   ├── __init__.py
│   ├── ui.py                              # login_page, inventory_page, auth_flow
│   ├── data.py                            # valid_user, locked_user (из .env)
│   └── api.py                             # api_client, auth_token
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                        # Маркеры, хуки (screenshot on failure и т.д.)
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── conftest.py                    # UI-специфичные фикстуры если нужны
│   │   └── test_login.py                  # test_login_valid_creds_redirects_to_inventory
│   │                                      # test_login_invalid_creds_shows_error
│   └── api/
│       ├── __init__.py
│       └── conftest.py                    # API-специфичные фикстуры если нужны
│
├── data/
│   ├── __init__.py
│   ├── users.py                           # @dataclass(frozen=True) UserData — тестовые юзеры
│   ├── messages.py                        # Ожидаемые тексты ошибок, заголовков, уведомлений
│   ├── factories/
│   │   └── __init__.py
│   └── payloads/
│       └── __init__.py
│
├── models/
│   ├── __init__.py
│   └── auth.py                            # AuthRequest, AuthResponse (dataclass / Pydantic)
│
└── utils/
    ├── __init__.py
    └── logger.py                          # get_logger(name) — единый конфиг логирования
```

---

## Поток данных

```
test_login.py
    │
    ├── auth_flow (fixture)  ← fixtures/ui.py
    │       │
    │       ├── LoginPage         ← app/pages/login_page.py
    │       │       └── BasePage  ← app/pages/base_page.py
    │       │
    │       └── InventoryPage     ← app/pages/inventory_page.py
    │               └── BasePage
    │
    ├── valid_user (fixture)  ← fixtures/data.py  ← data/users.py  ← .env
    │
    └── assert / expect()  ← только здесь, нигде больше
```

---

## Слои — кто что делает, кто что НЕ делает

| Слой | Делает | НЕ делает |
|------|--------|-----------|
| `tests/` | Arrange → Act → Assert | Локаторы, сетап, сырые Playwright-вызовы |
| `flows/` | Собирает шаги из нескольких страниц | Ассерты, прямые локаторы |
| `fixtures/` | Создаёт объекты, yield для teardown | Ассерты, хардкод данных |
| `app/pages/` | Локаторы (UPPER_SNAKE) + UI-действия | Ассерты, бизнес-логика |
| `app/components/` | Переиспользуемые куски UI | Ассерты |
| `app/api/` | HTTP-запросы, возвращает модели | Ассерты, Playwright-код |
| `config/` | URL, таймаут, браузер по среде | Бизнес-логика |
| `data/` | Замороженные датаклассы, константы | Логика, зависимость от среды |
| `models/` | Структуры запросов/ответов | Логика, Playwright |
| `utils/` | Чистые хелперы: логгер | API-логика, Playwright |

---

## Makefile — шорткаты

```makefile
.PHONY: install test smoke regression lint format trace clean

install:                          ## Установить зависимости
	poetry install

test:                             ## Все тесты
	poetry run pytest tests/ -v

smoke:                            ## Только smoke
	poetry run pytest tests/ -m smoke -v

regression:                       ## Только regression
	poetry run pytest tests/ -m regression -v

ui:                               ## Только UI тесты
	poetry run pytest tests/ui/ -v

api:                              ## Только API тесты
	poetry run pytest tests/api/ -v

headed:                           ## UI тесты с браузером (не headless)
	poetry run pytest tests/ui/ -v --headed

lint:                             ## Проверить код
	poetry run ruff check .

format:                           ## Отформатировать код
	poetry run ruff format .

trace:                            ## Прогон с trace (для дебага)
	poetry run pytest tests/ui/ -v --tracing on

clean:                            ## Удалить артефакты
	rm -rf artifacts/ .pytest_cache/ __pycache__/

help:                             ## Показать все команды
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
```

---

## Что изменилось vs. старая структура

| Что | Было | Стало | Зачем |
|-----|------|-------|-------|
| `__init__.py` | Отсутствовали | Во всех пакетах | Python-пакеты не резолвятся без них |
| `config/constants.py` | Не было | Добавлен | Место для ролей, статусов, лимитов |
| `data/users.py` | Данные только в `.env` | Frozen dataclasses | Типизированные тестовые данные, IDE подсказки |
| `data/messages.py` | Строки в тестах | Отдельный файл | Одно место правды для ожидаемых текстов |
| `app/api/base_api.py` | Пустая папка | Базовый HTTP-клиент | Фундамент для API-тестов |
| `models/auth.py` | Пустая папка | Типизированные модели | API возвращает модели, не dict |
| `tests/conftest.py` | Только корневой | + в tests/, tests/ui/, tests/api/ | Хуки и фикстуры по уровням |
| `header_component.py` | Так назывался | `header.py` | Компоненты без суффикса по конвенции |
| `login_flow.py` | Так назывался | `auth_flow.py` | Название по домену, а не по странице |
| `Makefile` | Не было | Добавлен | `make test` вместо `poetry run pytest tests/ -v` |
