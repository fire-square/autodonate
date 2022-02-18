SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy --install-types --non-interactive autodonate tests
#	poetry run flake8 .
	poetry run doc8 -q docs

.PHONY: unit
unit:
	cp config.toml.example config.toml
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit
