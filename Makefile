install:
	pip install -r requirements.txt

format:
	black ./schemas/*.py ./routes/*.py ./models/*.py ./config/*.py

lint:
	pylint --disable=R,C ./*/*.py

tests: 
	python3 -m pytest -vv -cov=./schemas/*py unit_tests.py