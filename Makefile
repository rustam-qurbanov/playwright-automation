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
