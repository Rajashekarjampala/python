# Write a python function to list all docker images available in the system.

import subprocess
def image_list(*images):
   find_img = subprocess.run(["docker images"])

   return find_img
print(image_list(list_of_images))

    
