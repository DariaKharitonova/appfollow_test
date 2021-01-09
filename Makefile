install:
	@poetry install

test:
	@poetry run pytest --cov-report term --cov-report xml --cov=news_parser news_parser tests

lint:
	@poetry run flake8 page_loader tests
	@poetry run mypy page_loader tests