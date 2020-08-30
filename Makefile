all: lint sphinx

lint:
	yamllint -s .
	flake8 .
	pydocstyle footy

sphinx:
	sphinx-build -b markdown . docs
