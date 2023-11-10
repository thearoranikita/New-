import os, sys
from pathlib import Path
import logging


while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

#src/__init__.py
#src/components/__init__.py
list_of_files = [
    f"{project_name}/__init__.py"
    f"{project_name}/components/__init__.py",
     f"{project_name}/config/__init__.py",
      f"{project_name}/constants/__init__.py",
       f"{project_name}/entity/__init__.py",
        f"{project_name}/exception/__init__.py", 
         f"{project_name}/logger/__init__.py",
          f"{project_name}/pipeline/__init__.py",
          f"{project_name}/utils/__init__.py",
          f"config/config.yaml",
          "schema.yaml",
          "app.py",
          "main.py",
          "logs.py",
          "exception.py",
          "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) #just aivai that filepath is made in teh windows system.
    filedir,filename = os.path.split(filepath)  #for "data/file" -- filedir is the data and filename is the file.

    if filedir != "":  #checking if filedirectory is present or not - if filedrir not present make a new one. 
        os.makedirs(filedir,exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #if filename doesnt exist or is empty make a new file
        with open(filepath,"w") as f:  #we arent writing anything to the filen now. just making it. the xtension of the file will depend on whats imported. 
            pass

    else:
        logging.info("file is already present at : {filepath}")

        