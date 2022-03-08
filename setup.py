from setuptools import setup, find_packages

setup(
    name="GeneralAPIWrapper",
    version="0.1.6",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
    ],
)
