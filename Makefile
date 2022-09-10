.PHONY: environment lint test

environment:
	sorce venv3.6/bin/activate
lint:
	flake8 pylog/  tests/ --ignore=W293,E402 --count
test:
	coverage run --source pylog --parallel-mode -m unittest
	coverage combine
	coverage report

