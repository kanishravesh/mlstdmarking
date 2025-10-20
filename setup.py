from setuptools import setup, find_packages  # type: ignore[import]
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str)-> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirement=[]
    with open(file_path, 'r') as fileobj:
        requirement = fileobj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]

        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)

    return requirement

setup(
    name="ml_project",
    version="0.0.1",
    author="kanish",
    author_email="kanishravesh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)