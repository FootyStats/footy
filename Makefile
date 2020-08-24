all: lint sphinx

lint:
	flake8 .
	pydocstyle footy

sphinx:
	sphinx-build -b markdown . docs
