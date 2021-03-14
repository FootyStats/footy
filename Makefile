all: lint test sphinx build

build:
	jupyter-nbconvert --execute --no-input --to pdf Footy.ipynb

lint:
	yamllint -s .
	flake8 .
	pydocstyle footy

sphinx:
	sphinx-build -b markdown . docs

test:
	PYTHONPATH=.:.. pytest --cov=footy --verbose
