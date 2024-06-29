from setuptools import find_packages,setup
from typing import List

HYPEN="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)



setup(

    name="Ml project",
    version="0.0.1",
    author="Rudra",
    author_email= "rudrashamra129@gmail.com",
    packages=find_packages(),
    install_require =get_requirements("requirements.txt")

)