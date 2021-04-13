import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylog",
    version="0.0.3",
    author="Michael Kerry",
    author_email="michael_kerry@harvard.edu",
    description="A utility for python logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.huit.harvard.edu/HUIT/pylog",
    project_urls={
        "Bug Tracker": "https://github.huit.harvard.edu/HUIT/pylog/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7"
)
