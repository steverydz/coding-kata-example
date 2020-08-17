install:
	pip install -r requirements.txt

test:
	pytest app.py

test-watch:
	ptw app.py
