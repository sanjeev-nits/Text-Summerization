import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "https://github.com/sanjeev-nits/Text-Summerization.git"
AUTHOR_USER_NAME = "SanjeevKumar-01"
AUTHOR_EMAIL = "sanjeevkumar814155@gmail.com"
SRC_REPO = "textsummerizer"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summerization",
    long_description=long_description,

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)