import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SinhalaTokenizer", # Replace with your own username
    version="0.0.1",
    author="Maleesha Kumarage",
    description="A language processing tool for Sinhalese (සිංහල)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaleeshaKumarage/SinhalaTokenizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['emoji'],
)