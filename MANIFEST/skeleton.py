from setuptools import setup, find_packages

setup(
    name="fastapi-skeleton",
    version="1.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
    ],
)
