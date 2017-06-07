import os

#let's create directory
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

#let's write given data to any file we want
def write_in_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
