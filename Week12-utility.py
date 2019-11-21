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
    
def UpdateString(string_1, string_2, int_1):
    list_new = []
    for char in string_1:
        list_new.append(char)
    list_new[int_1] = string_2
    string_new = ''.join(list_new)
    PrintOutput(string_new)

def FindWordCount(list_words, string):
    word_count = 0
    for small_string in list_words:
        for i in range(len(small_string)):
            if small_string[i:((len(string)) + i)] == string:
                word_count += 1
    return word_count
