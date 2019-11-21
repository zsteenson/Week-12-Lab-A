#   https://github.com/zsteenson/Week-12-Lab-A
#   Zach Steenson 
#  ​CSCI 102 – Section A 
#   Week 11 - Part A

def PrintOutput(a):
    print('OUTPUT', a)

def LoadFile(file):
    f = open(file, "r")
    string = f.read()
    list_string = string.split("\n")
    return list_string
    f.close()
