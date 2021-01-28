# file-output.py
f = open('Save.txt','a')
f.write('hello world')
f.close()

#append a line to a text file
with open("Save.txt", "a") as f:
    f.write("new line\n")

#If you want to preprend something you have to read from the file first:
with open("Save.txt", "r+") as f:
    old = f.read() # read everything in the file
    f.seek(0) # rewind
    f.write("new line\n" + old) # write the new line before