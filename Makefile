clean_pyc:
	@find . -name "*.pyc" -exec rm {} +

new_venv:
	#@virtualenv venv
	@python3 -mvenv venv

install:
	@source venv/bin/activate; pip install -e .

init: new_venv
	@source venv/bin/activate; pip install --upgrade pip
	$(MAKE) install

clean:
	@rm -rf dist build

dist: clean
	@source venv/bin/activate; pip install --upgrade setuptools wheel
	@source venv/bin/activate; python setup.py sdist bdist_wheel

publish: dist
	@source venv/bin/activate; pip install --upgrade twine
	@source venv/bin/activate; twine upload dist/*
