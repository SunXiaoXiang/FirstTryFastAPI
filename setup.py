from setuptools import setup, find_packages

setup(
    name="FirstTryFastAPI",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "pytest",
        "httpx",
    ],
)