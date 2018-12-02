#!/usr/bin/make -f

install-test-requirements:
	pip install -U pip pipenv
	pipenv install --editable .
	pipenv install --dev

test-python:
	@echo "Running Python tests"
	pipenv run python setup.py -q test || exit 1
	@echo ""

lint-python:
	@echo "Linting Python files"
	flake8 --ignore=E501,E731 --exclude=.git,compat.py mocket
	@echo ""

init: install-test-requirements
	pipenv check

test: install-test-requirements lint-python test-python

test-ci: install-test-requirements lint-python
	mkdir -p shippable/testresults
	mkdir -p shippable/codecoverage
	pipenv run python runtests.py --junitxml=shippable/testresults/nosetests.xml \
	--cov-report=xml:shippable/codecoverage/coverage.xml

safetest:
	export SKIP_TRUE_REDIS=1; export SKIP_TRUE_HTTP=1; make test

publish:
	pipenv run python setup.py sdist upload
	pipenv install anaconda-client
	anaconda upload dist/mocket-$(shell python -c 'import mocket; print(mocket.__version__)').tar.gz

clean:
	rm -rf dist
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} \;

.PHONY: clean publish safetest test test-ci init lint-python test-python install-test-requirements

