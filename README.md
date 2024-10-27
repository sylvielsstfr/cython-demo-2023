Demonstrating Cython, using both normal and pure Python syntax, using Conway's Game Of Life.
Adapted to be run with a pyproject.toml (Sylvie Dagoret-Campagne) for the 3 components
- unoptimized
- cython
- pure-python-mode
License: MIT

To install 
    python -m pip cache purge

    pip install -e .
    or
    pip install .


To run the appls do:
       python src/unoptimized/main.py 
       python src/cythonmode/main.py 
       python src/purepythonmode/main.py 