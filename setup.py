from setuptools import find_packages
from setuptools import setup


setup(
    name="deployer",
    version="0.1",
    packages=find_packages(exclude=["venv"]),
    entry_points={
        "console_scripts": [
            "deployer = deployer.main:main"
        ]
    }
)
