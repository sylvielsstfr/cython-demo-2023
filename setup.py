import numpy
from setuptools import setup,Extension,find_packages
from Cython.Build import cythonize

ext_modules = [
    Extension("unoptimized.life", 
              ["src/unoptimized/life.py"],
              include_dirs=[numpy.get_include()],
              define_macros=[("CYTHON_LIMITED_API","1")],
              py_limited_api=True,
              ),
    Extension("cythonmode.life", 
              ["src/cythonmode/life.pyx"],
              include_dirs=[numpy.get_include()],
              define_macros=[("CYTHON_LIMITED_API","1")],
              py_limited_api=True,
              ),
    Extension("purepythonmode.life", 
              ["src/purepythonmode/life.py"],
              include_dirs=[numpy.get_include()],
              define_macros=[("CYTHON_LIMITED_API","1")],
              py_limited_api=True,
              ),
]

setup(ext_modules = cythonize(ext_modules),
      include_dirs=[numpy.get_include()],
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      compiler_directives={"language_level": 3, "profile": False},
      )