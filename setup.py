import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.head()

setuptools.setup(
    name="example-pkg-neilmauricio", # Replace with your own username
    version="0.0.1",
    author="Neil Mauricio",
    author_email="neil.mauricio@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
 )
