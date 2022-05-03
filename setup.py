import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description  =fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USURNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
            "Programming Language :: Python ::3",
            "Licence ::OSI Approved :: MIT Licence",
            "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)




