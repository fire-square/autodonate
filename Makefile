SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run black .
	poetry run mypy --install-types --non-interactive autodonate tests
	poetry run doc8 -q docs

.PHONY: unit
unit:
	poetry run python manage.py migrate
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit
