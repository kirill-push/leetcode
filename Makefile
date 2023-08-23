SHELL=/bin/bash

.PHONY: all
all:
	$(MAKE) --keep-going black isort flake8 mypy pytest

.PHONY: .poetry_install
.poetry_install:
	poetry install

.PHONY: black
black: .poetry_install
	poetry run black --check .

.PHONY: isort
isort: .poetry_install
	poetry run isort --check .

.PHONY: mypy
mypy: .poetry_install
	poetry run mypy .

.PHONY: flake8
flake8: .poetry_install
	poetry run flake8

.PHONY: pytest
TESTS_ARGS=
pytest: .poetry_install
	poetry run pytest -v tests $(TESTS_ARGS)

.PHONY: shell
shell:
	poetry shell
