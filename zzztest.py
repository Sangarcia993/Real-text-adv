#https://programminghistorian.org/en/lessons/working-with-text-files

# BUEN EJEMPLO = https://github.com/Victoria-Hodder/pyladies-text-adventure

# Anda a Github busca text adv y copia

import os

with os.scandir('text-files/') as entries:
    for entry in entries:
        print(entry.name)


"""
# file-output.py
f = open('text-fileslol.txt','a')
f.write('hello world')
f.close()


#read and prints whats is in the file
f = open("Save.txt", "r")
file = f.read()
print(file)

#append a line to a text file
with open("Save.txt", "a") as f:
    f.write("new line\n")

#If you want to preprend something you have to read from the file first:
with open("Save.txt", "r+") as f:
    old = f.read() # read everything in the file
    f.seek(0) # rewind
    f.write("new line\n" + old) # write the new line before
"""