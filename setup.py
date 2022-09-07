from setuptools import setup, find_packages

setup(
    name="webhook-testing",
    version="0.1.0",  # TODO: Figure out how to sync with src/_version.py
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["fastapi", "secure", "uvicorn"],
)
