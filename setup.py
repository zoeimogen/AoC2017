import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AoC2017",
    version="0.0.1",
    author="Zoe O'Connell",
    author_email="zoe@complicity.co.uk",
    description="Advent of Code 2017 solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zoeimogen/AoC2017",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ],
)