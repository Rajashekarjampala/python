'''
Write a Function to list all running docker containers in the host machine

:param *args passing by the user type string only
:return the list of images
'''
# import docker module
import docker
# import the subprocess
import subprocess
# import popen,PIPE from subprocess
from subprocess import Popen,PIPE

# define function 
def check_cont(*containers):

    # By using this command to find the list of running containers from the host VM
    list_cont=subprocess.Popen(["docker ps -a"], stdout=PIPE,shell=True)
    # return the list of running containers 
    return list_cont

# finally return list of runnung containers
result=check_cont(list_of_cont)
print(result)   






