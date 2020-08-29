all: lint test sphinx

lint:
	flake8 .
	pydocstyle footy

sphinx:
	sphinx-build -b markdown . docs

test:
	PYTHONPATH=.. coverage run -m pytest -v --durations=3 tests
	coverage report
