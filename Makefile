SHELL:=/usr/bin/env bash

.PHONY: lint
lint: style

.PHONY: style
style:
	poetry run black .
	poetry run isort .
	poetry run pycln . --config setup.cfg
	poetry run mypy --install-types --non-interactive autodonate tests
	poetry run flake8 .
	poetry run doc8 -q docs

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run safety check --full-report

.PHONY: test
test: style package unit
