import setuptools

# read the readme.md file and 
# add it as the
# long description of our package
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lol", # Replace with your own username
    version="0.0.1",
    author="P Pranav Baburaj",
    author_email="code-roller@googlegroups.com",
    description="A simple json database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranavbaburaj/lol-db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)