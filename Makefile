SHELL:=/usr/bin/env bash

.PHONY: lint
lint: style

.PHONY: style
style:
	poetry run black .
	poetry run isort .
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

.PHONY: docker
docker:
	docker build -t autodonate .

.PHONY: test
test: style package unit
