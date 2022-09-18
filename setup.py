"""Setup module for PyPI / pip integration.
"""

import cutie
import setuptools

with open("readme.md", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()


setuptools.setup(
    name="cutie",
    version=cutie.__version__,
    author=cutie.__author__,
    author_email="contact.kamik423@gmail.com",
    description=cutie.__doc__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/kamik423/cutie",
    py_modules=["cutie"],
    license=cutie.__license__,
    install_requires=["colorama", "readchar!=3.0.5"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
