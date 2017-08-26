main: venv crops
	@echo nothing yet

venv:
	python3 -m venv venv
	venv/bin/pip install pillow numpy

crops:
	mkdir crops
	venv/bin/python -u cropper.py
