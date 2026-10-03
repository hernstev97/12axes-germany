.PHONY: all status check-loop

all:
	python pipeline/loop.py all

status:
	python pipeline/loop.py status

check-loop:
	python -m unittest discover -s pipeline/tests -p 'test_loop.py'
