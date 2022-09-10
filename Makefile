.PHONY: environment lint test

environment:
	sorce venv3.6/bin/activate
lint:
	flake8 PyLog/  test/ --ignore=W293 --count
test:
	coverage run --source pylog --parallel-mode -m unittest
	coverage combine
	coverage report

