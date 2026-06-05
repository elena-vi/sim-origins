POETRY ?= poetry

.DEFAULT_GOAL := all

.PHONY: all build check fix test

all: fix test build

fix:
	$(POETRY) run ruff check . --fix
	$(POETRY) run ruff format .

test:
	$(POETRY) run pytest

build:
	$(POETRY) build
	$(POETRY) run python tools/build_ts4script.py

check:
	$(POETRY) run ruff check .
	$(POETRY) run ruff format --check .
