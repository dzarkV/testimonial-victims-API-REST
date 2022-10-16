install:
	pip install -r requirements.txt

format:
	black ./schemas/*.py ./routes/*.py ./models/*.py ./config/*.py

lint:
	pylint --disable=R,C,W0622 *.py **/*.py

tests: 
	python3 -m pytest -vv unit_tests.py