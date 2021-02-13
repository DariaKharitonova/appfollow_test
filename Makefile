install:
	@poetry install

test:
	@poetry run pytest -vv

lint:
	@poetry run flake8 page_loader tests
	@poetry run mypy page_loader tests