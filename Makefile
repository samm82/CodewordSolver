PY = python
PYFLAGS = 

SRC = src/Main.py

.PHONY: all

main: 
	$(PY) $(PYFLAGS) $(SRC)

all: main
