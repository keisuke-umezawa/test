from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ipad-test-framework",
    version="0.1.0",
    author="Keisuke Umezawa",
    author_email="keisuke.umezawa@gmail.com",
    description="A testing framework for iPad devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keisuke-umezawa/test",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.0.0",
    ],
)
