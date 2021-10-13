import os
def create_script(filename):
  comments = "# Start of a new Python program"

  with open(filename,'w') as this_file:
    for l in comments:
      this_file.write(l)

  with open(filename,'r') as f:
    x = f.read()
  print(x)

  filesize = os.path.getsize(filename)
  return'file size: {}'.format(filesize)

print(create_script("just_fun.py"))