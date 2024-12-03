from setuptools import setup, find_packages

setup(
    name="update-gempa-indonesia",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'update-gempa-indonesia=update-gempa-indonesia.__main__:main',
        ],
    },
)
