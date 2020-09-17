import setuptools
import re

ex = re.compile("..version.. = \'(.*?)\'")

with open("README.md", "r") as f:
    long_description = f.read()

with open("PyBlox2/__init__.py", "r") as f:
    version = ex.findall(f.read())[0]

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setuptools.setup(
    name="Kyandle",
    version=version,
    author="Kyando",
    author_email="amehikoji@gmail.com",
    description="Parser for the Kyandle (.kya) syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kyando2/candle",
    packages=setuptools.find_packages(),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)