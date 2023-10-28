from setuptools import setup, find_packages
import shutil

# Package metadata
name = "astra-document"
version = "1.0.0"  # Update with your package's version number
description = "Provides you with high level functions to interact with the Datastax API's HTTP verbs."
author = "Andrea Licheri"
author_email = "public@andrealicheri.anonaddy.me"
url = "https://github.com/andrealicheri/astra-document"

# Define your package's dependencies
install_requires = [
    "requests",
    "python-dotenv"
]

# Other package-related settings
packages = find_packages()
classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries :: Python Modules",
]



# Setup function
setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    install_requires=install_requires,
    packages=packages,
    classifiers=classifiers,
)

shutil.rmtree("astra_document.egg-info")
shutil.rmtree("build")