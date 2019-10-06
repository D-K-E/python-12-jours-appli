import os
import setuptools


# currentdir = os.getcwd()

with open("README.rst", "r", encoding="utf-8") as f:
    long_desc = f.read()

with open("LICENSE", "r", encoding="utf-8") as f:
    license_str = f.read()

setuptools.setup(
    name="12-jours-appli",
    version="0.1",
    author='Kaan Eraslan',
    python_requires='>=3.5.0',
    author_email="kaaneraslan@gmail.com",
    description="Application Finale de Python en 12 jours",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    license=license_str,
    url="https://github.com/D-K-E/python-12-jours-appli/",
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*",
                 "docs", ".gitignore", "README.rst"]
    ),
    test_suite="tests",
    install_requires=[
        # "numpy",
        "pillow",
        "lxml",
        "PySide2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
)
