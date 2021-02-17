
from distutils.core import setup

setup(
    name="pybundle",
    version="master",
    author="munchkinhalfling",
    # author_email="",
    # url="",
    description="A project-level package manager for PyPI packages",
    packages=["pybundle", "pybundle.templates", "pybundle.util"],
    scripts=['pyb']
)
        