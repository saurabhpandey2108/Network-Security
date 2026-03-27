'''
The setup.py file is an essential part of any Python project. 
It is used to package and distribute the project, and it also contains
metadata about the project.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirements_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as requirements_file:
            # Read lines from the file
            lines = requirements_file.readlines()
            # Process each line
            for line in lines:
                requirements = line.strip()
                # Skip empty lines and -e . 
                if requirements and not requirements.startswith('-e .'):
                    requirements_list.append(requirements)
           
    except FileNotFoundError:
        raise Exception("requirements.txt not found")
    return requirements_list
    
print(get_requirements())

setup(
    name='Network-Security',
    version='0.1.0',
    author ='Saurabh Pandey',
    author_email='[saurabhpandey59254@gmail.com]',
    packages=find_packages(),
    install_requires=get_requirements()
)