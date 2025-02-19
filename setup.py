from setuptools import setup, find_packages

setup(
    name="bornvita",
    version="0.1.1",
    author="Raghav Dadhich",
    author_email="dadhichraghav896@gmail.com",
    description="A package that displays bornvita brainrot content on the entire screen",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/raghav3615/bornvita",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bornvita=bornvita.brainrot:generate_brainrot"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
