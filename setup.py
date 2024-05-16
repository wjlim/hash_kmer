from setuptools import setup, Extension
from Cython.Build import cythonize

extension = Extension(
    "kmer_hashing",
    sources=["kmer_hashing.pyx"],
    extra_compile_args=['-O2', '-fPIC'],  # Adjust or remove flags as necessary
)

setup(
    ext_modules=cythonize(extension)
)