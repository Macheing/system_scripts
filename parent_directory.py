'''
The parent_directory function returns the name of the 
directory that's located just above the current working 
directory
'''

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  current = os.getcwd()
  #print(path)
  abspath = os.path.dirname(os.path.dirname(current))
  # Return the absolute path of the parent directory
  return abspath

print(parent_directory())