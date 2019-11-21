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

def ScoreFinder(list_1, list_2, string):
    list_1_lower = []
    for small_list in list_1:
        list_1_lower.append(small_list.lower())
    if string in list_1_lower or string in list_1:
        for i in range(len(list_1_lower)):
            if list_1_lower[i] == string or list_1[i] == string:
                PrintOutput("%s got a score of %d" % (list_1[i], list_2[i]))
    else:
        PrintOutput("player not found")

def Union(list_1, list_2):
    list_union = list_1 + list_2
    return list_union

def Intersection(list_1, list_2):
    intersection_list = []
    for char in list_1:
        if char in list_2:
            intersection_list.append(char)
    return intersection_list

def Notin(list_1, list_2):
    notin_list = []
    for char in list_1:
        if not(char in list_2):
            notin_list.append(char)
    return notin_list
