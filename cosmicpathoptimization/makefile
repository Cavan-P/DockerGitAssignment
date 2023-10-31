check_types:
	mypy --disallow-untyped-defs --strict main.py test_main.py

run:
	python main.py

run_local_test:
	cat 1.in | python main.py | diff - 1.ans
	@echo "Passed local test"

style:
	flake8 main.py
	flake8 test_main.py

fix_style:
	autopep8 --in-place --aggressive --aggressive main.py test_main.py

unittest:
	pytest test_main.py

kattis:
	kattis -p cosmicpathoptimization -f main.py

all: fix_style style unittest run_local_test check_types kattis