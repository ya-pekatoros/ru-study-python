SHELL=/bin/bash -O globstar -c

lint:
	black --check --diff .
	flake8 --max-complexity 10
	mypy --sqlite-cache .

test:
	pytest

check: lint test

format_code:
	black .
