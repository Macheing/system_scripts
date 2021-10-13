import os
import csv

'''
We're working with a list of flowers and some information about each one. 
The create_file function writes this information to a CSV file. The 
contents_of_file function reads this file into records and returns 
the information in a nicely formatted block
'''

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ''
  # Call the function to create the file 
  create_file(filename)
  # Open the file
  with open(filename,'r') as file:
    # Read the rows of the file into a dictionary
    data = csv.DictReader(file)
    # Process each item of the dictionary
    for row in data:
      	name,color,types = row['name'],row['color'],row['type']
	#print(name,color,types)
      	return_string += "a {} {} is {}\n".format(color, name, types)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
