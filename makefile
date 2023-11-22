install:
	poetry install

lint:
	poetry run flake8 scripts

format:
	poetry run black scripts
