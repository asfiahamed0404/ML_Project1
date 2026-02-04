from setuptools import setup, find_packages
#from typing import List -- old way

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->list[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()      # Reads all lines from the file,Returns a list of strings,Each line ends with \n (newline character)
        requirements = [req.strip() for req in requirements]  #requirements = [req.replace("\n","") for req in requirements] - old way
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
  



setup(
    name="mlproject",
    version="0.0.1",
    author="Asfi",
    author_email="muasfiahamed276@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)