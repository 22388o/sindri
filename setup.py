#!/usr/bin/env python3
"""
Setup script for Sindri.
"""

from pathlib import Path

import setuptools


PROJECT_NAME = "sindri"


with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

version = {}
with open(Path("src") / PROJECT_NAME / "_version.py",
          "r", encoding="utf-8") as version_file:
    exec(version_file.read(), version)


setuptools.setup(
    name=PROJECT_NAME,
    version=version["__version__"],
    author="C.A.M. Gerlach and the HAMMA group",
    author_email="CAM.Gerlach@Gerlach.CAM",
    description=("A package for data logging and management "
                 "of HAMMA lightning sensors."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="iot lightning sensor remote control research m2m server web",
    url=f"https://github.com/hamma-dev/{PROJECT_NAME}",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        "lektor>=3.1",
        "matplotlib",
        "numpy",
        "pandas",
        ],
    entry_points={
        "console_scripts": [
            f"{PROJECT_NAME}={PROJECT_NAME}.__main__:main"]
        },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Environment :: No Input/Output (Daemon)",
        "Framework :: Lektor",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: System :: Monitoring",
        ],
    )
