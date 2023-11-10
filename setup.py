
from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is our machine learning project in modular coding"
AUTHOR_NAME = "Nikita Arora"
AUTHOR_EMAIL= "nikitaarora452@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."  #this is written in txt file to import setup.py file. 

# Requiremnets.txt file open
# read that file 
#replace \n -- it is hidden at the end of each requirement. 

def get_requirements_list()->List[str]: #just to infrom that output is a list of strings 
    with open(REQUIREMENTS_FILE_NAME) as requirement_file: #opening the file
        requiremnet_list = requirement_file.readlines() #reading line by line 
        requiremnet_list = [requirement_name.replace("\n","") for requirement_name in requiremnet_list] #using list comprehension, replacing hidden \n by mepty.

        if HYPHEN_E_DOT in requiremnet_list:
            requiremnet_list.remove(HYPHEN_E_DOT)


        return requiremnet_list

    
setup(name=PROJECT_NAME, #setup helps in building the package of your projevt 
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL, 
      packages=find_packages(), #packages will go to main project folder (in this case src) and will find __init__.py file there.
      install_requries = get_requirements_list() #matlab yeh requirements chahiye yeh package chalane ke liye
     )