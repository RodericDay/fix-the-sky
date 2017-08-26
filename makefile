main: venv
	@echo nothing yet

venv:
	python3 -m venv venv
	venv/bin/pip install pillow numpy
