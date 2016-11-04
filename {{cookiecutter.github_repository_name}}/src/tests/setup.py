from setuptools import setup, find_packages

setup(
    name = "{{cookiecutter.app_name}}_tests",
    version = "0.1",
    author = "{{cookiecutter.github_username}}",
    author_email = "{{cookiecutter.email}}",
    packages=find_packages(),
)

