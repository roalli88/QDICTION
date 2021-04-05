from setuptools import setup

setup(
    name="QDiction",
    version="1.0",
    author="Rasaq O Alli",
    author_email="ro_alli@protonmail.com",
    description="A minimal lightweight dictionary based on wordnet",
    long_description=open("README.rst", 'r').read(),
    url="https://github.com/roalli88/QDICTION",
    license="GPL.v.3",
    keywords="dictionary wordnet english",
    project_urls={
        "Source Code": "https://github.com/roalli88/DICTIONARY"
        },
    packages=["qdiction", "qdiction.icons", "qdiction.nltk_data"],
    install_requires=["PyQt5 >= 5.10", "nltk"],
    python_requires=">=3.6",
    package_data={
        "qdiction.icons": ["*.png"],
        "qdiction.nltk_data": ["*"],
        "": ["*.txt", "*.rst"],
        },
    entry_points={
        "console_scripts": [
            "qdiction = qdiction.__main__:main"
            ]
        }

)
