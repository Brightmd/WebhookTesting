from setuptools import setup, find_packages

from webhooktesting._version import __version__

setup(
    name="webhook-testing",
    version=__version__,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["fastapi", "secure", "uvicorn"],
)
