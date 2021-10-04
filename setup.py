import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="bank_base_gt",
    version="0.1.1",
    author="Carlos Simon",
    author_email="dev@csimon.dev",
    description="Bank Parser Base Package for banks in Guatemala",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gt-banks-parser/banks-parser-base",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "Topic :: Office/Business :: Financial",
        "Topic :: Utilities"
    ],
    python_requires=">=3.6",
    install_requires=["requests", "bs4", "money", "babel"],
)