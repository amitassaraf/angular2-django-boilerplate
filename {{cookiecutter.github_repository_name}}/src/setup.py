from setuptools import setup, find_packages

setup(
    name = "{{cookiecutter.app_name}}",
    version = "0.1",
    author = "{{cookiecutter.github_username}}",
    author_email = "{{cookiecutter.email}}",
    description = ("{{cookiecutter.description}}"),
    packages=find_packages(),
)

