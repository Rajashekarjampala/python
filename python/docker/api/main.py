'''
Write a Function to list all docker images in the host machine

:param *args passing by the user
:return the list of images
'''

# import docker module
import docker
# import the subprocess
import subprocess
# import popen,PIPE from subprocess
from subprocess import Popen,PIPE

# define function 
def check_images(*images):

    # By using this command to find the list of images from the host VM
    list_images=subprocess.Popen(["docker image ls"], stdout=PIPE,shell=True)
    # return the list of images
    return list_images

# function calling    
result=check_images(list_of_images)    
print(result)
