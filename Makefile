repro:
	python3 cli.py --tex paper.tex

reproduce:
	python3 cli.py --tex paper.tex

dev:
	python cli.py

test:
	python3 -m unittest discover -s tests -v
