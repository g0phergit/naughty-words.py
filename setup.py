import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="naughty_words_py",
    version="0.0.1",
    author="Gopher",
    author_email="gopherubuntouch@gmail.com",
    description="Naugty words parser for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/g0phergit/naughty-words.py",
    project_urls={
        "Bug Tracker": "https://github.com/g0phergit/naughty_words.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
