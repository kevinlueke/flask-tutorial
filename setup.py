import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="flask-tutorial"
    version="0.0.1",
    author="Kevin Lueke",
    author_email="kevinlueke66@gmail.com",
    description="Tutorial on Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

