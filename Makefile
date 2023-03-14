build:
	poetry build
install:
	pip install --force-reinstall dist/hexlet_code-0.1.0.tar.gz
lint:
	poetry run flake8 gendiff/
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
