#https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="latest-indonesia-earthquake",
    version="0.0.1",
    author="ahmad sopyan",
    author_email="madsopyan5@gmail.com",
    description="this package will get the latest earthquake from BMKG -Meteorology, Climatology, and Geophysics Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madshopy/latest-indonesia-earthquake",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",

    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",



# gunakan code ini di terminal untuk : menginstal atau memperbarui modul build di Python.
# Modul build adalah alat yang digunakan untuk membangun (build) paket Python dari proyek Anda,
# py -m pip install --upgrade build
# py -m build
#https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives
)

