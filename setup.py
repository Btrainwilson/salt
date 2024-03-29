import os
from setuptools import setup, find_packages


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    file = open(filepath, "r")
    return file.read()


setup(
    name="salt",
    version="0.0.1",
    author="Blake Wilson",
    author_email="wilso692@purdue.edu",
    description="",
    long_description=read("README.rst"),
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords=[],
    entry_points={
        "console_scripts": [
            "salt = salt:main",
            "srf = salt.rotate_files:main",
            "shp = salt.http_server:main",
        ]
    },
    url="",
    packages=find_packages(),
    scripts=["bash/mm", "bash/ltf", "bash/sno"],
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
