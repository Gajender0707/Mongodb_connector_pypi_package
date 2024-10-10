from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

def Requirements(filename):
    with open(filename,"r") as f:
        req=f.readlines()
        req=[i.replace("\n","") for i in req]
        if "-e ." in req:
            req.remove("-e .")
    return req



__version__ = "0.0.1"
REPO_NAME = "mongodb_connector_pypi_package"
PKG_NAME= "mongo_connect"
AUTHOR_USER_NAME = "Gajender"
AUTHOR_EMAIL = "iamsanju0707@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=Requirements("requirements.txt")
    )
