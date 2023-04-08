.PHONY:  lint test

lint:
	flake8 pylog/ tests/ example/ --ignore=W293,E402 --max-line-length=127 --count
test:
	coverage run --source pylog --parallel-mode -m unittest
	coverage combine


