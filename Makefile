clean_pyc:
	@find . -name "*.pyc" -exec rm {} +

new_venv:
	@virtualenv venv

install:
	@source venv/bin/activate; pip install -e . --process-dependency-links

init: new_venv
	@source venv/bin/activate; pip install --upgrade pip
	@source venv/bin/activate; pip install -e . --process-dependency-links
