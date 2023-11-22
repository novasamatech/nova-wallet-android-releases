# Variables
PYTHON := python
PYTHON_VERSION := 3.11
VENV ?= .venv

install: venv .create-venv requirements

venv:
	$(PYTHON) -m venv .venv

.create-venv:
	test -d $(VENV) || python$(PYTHON_VERSION) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install poetry

requirements:
	$(VENV)/bin/poetry install --no-root
	. .venv/bin/activate

lint:
	poetry run flake8 scripts

format:
	poetry run black scripts

fetch-comment:
	$(VENV)/bin/python scripts/fetch_comment_body.py $(COMMENT_LINK) $(VERSION)

update-version:
	$(VENV)/bin/python scripts/version_updater.py $(VERSION) $(TIME) $(SEVERITY)
