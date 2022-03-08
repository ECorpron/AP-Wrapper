from setuptools import setup, find_packages

setup(
    name="API_Wrapper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.27.1",
    ],
)
