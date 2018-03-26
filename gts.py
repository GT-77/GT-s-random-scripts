#NOTE# this module has been made by GT ~ 77 (discord tag: GT ~ 77#3141)                   #NOTE#
#NOTE# just a bunch of simple functions that i use regularly                              #NOTE#
#NOTE# i do not guarantee all of them to work perfectly, report any glitches              #NOTE#
import random                                                                             #NOTE#
#NOTE# ^ because random is useful                                                         #NOTE#
#NOTE# i use the string "N/A = VOID = EMPTY" as a checker if no argument was given        #NOTE#
#NOTE# a cool thing is that none of the functions depend on eachother                     #NOTE#
# version 1.0.0

#NOTE##NOTE##NOTE##NOTE#
#NOTE#  GROUP  1  #NOTE#
#NOTE##NOTE##NOTE##NOTE#

def combo_print(input1 = "N/A = VOID = EMPTY"):
    """prints all elements in the input1 list, in order"""
    if type(input1) == list:
        for element in input1:
            print(element)
    elif input1 == "N/A = VOID = EMPTY":
        pass
    else:
        print(input1)
def randomize(input1 = "N/A = VOID = EMPTY", input2 = ""):
    """returns a random element from the list "input1"
       if the list is empty, the second input is returned"""
    if type(input1) == list and input1 != []:
        return(input1[random.randint(0, len(input1) - 1)])
    elif type(input1) == list or input1 == "N/A = VOID = EMPTY":
        return(input2)
    else:
        return(input1)
def memorize(input1 = "N/A = VOID = EMPTY", input2 = ""):
    """returns the first element from the list "input1"
       removes the said element from the list
       if the list is empty, the second input is returned"""
    if type(input1) == list and input1 != []:
        memory = input1[0]
        del(input1[0])
        return(memory)
    elif type(input1) == list or input1 == "N/A = VOID = EMPTY":
        return(input2)
    else:
        return(input1)
def randomize_and_memorize(input1, input2 = ""):
    """returns a random element from the list "input1"
       removes the said element from the list
       if the list is empty, the second input is returned"""
    if type(input1) == list and input1 != []:
        dice = random.randint(0, len(input1) - 1)
        memory = input1[dice]
        del(input1[dice])
        return(memory)
    elif type(input1) == list or input1 == "N/A = VOID = EMPTY":
        return(input2)
    else:
        return(input1)
def complex_randomize(input1, input2 = ""):
    """receives as first input a list of tuples
       each tuple containing 2 elements:
           - the first element is an integer defining the chance of the second element being chosen (relative to the sum of all other integers)
           - the second element can be whatever you like
       returns a random second element from each tuple, depending on the weight defined by the first element of each tuple
       in case that is hard to digest, here are two examples:
       1.
           receives the list [(99, "one"), (1, "two")]
           has a 99% chance of returning "one", and a 1% chance of returning "two"
       2.
           receives the list [(12, "yellow"), (7, "red"), (1, "void")]
           has a 60% chance of returning "yellow", 35% chance of returning "red", and 5% chance of returning "void"
       if the first input is an empty list, second input is returned"""
    if type(input1) == list and input1 != []:
        output1 = []
        for element in input1:
            if type(element) != tuple:
                output1.append(element)
            else:
                if type(element[0]) == int:
                    for times in range(element[0]):
                        output1.append(element[1])
        return(output1[random.randint(0, len(output1) - 1)])
    elif type(input1) == list or input1 == "N/A = VOID = EMPTY":
        return(input2)
    else:
        return(input1)
def complex_randomize_and_memorize(input1, input2 = ""):
    """receives as first input a list of tuples
       each tuple containing 2 elements:
           - the first element is an integer defining the chance of the second element being chosen (relative to the sum of all other integers)
           - the second element can be whatever you like
       returns a random second element from each tuple, depending on the weight defined by the first element of each tuple
       in case that is hard to digest, here are two examples:
       1.
           receives the list [(99, "one"), (1, "two")]
           has a 99% chance of returning "one", and a 1% chance of returning "two"
       2.
           receives the list [(12, "yellow"), (7, "red"), (1, "void")]
           has a 60% chance of returning "yellow", 35% chance of returning "red", and 5% chance of returning "void"
       the tuple from which that element has been chosen is removed from the list
       if the first input is an empty list, second input is returned"""
    if type(input1) == list and input1 != []:
        output1 = []
        for element in input1:
            if type(element) != tuple:
                output1.append(element)
            else:
                if type(element[0]) == int:
                    for times in range(element[0]):
                        output1.append(element[1])
        dice = random.randint(0, len(output1) - 1)
        counter = -1
        for element in input1:
            counter += 1
            if type(element) == tuple:
                if element[1] == output1[dice]:
                    del(input1[counter])
            else:
                if element[1] == outpu1[dice]:
                    del(input1[counter])
        return(output1[dice])
    elif type(input1) == list:
        return(input2)
    else:
        return(input1)



#NOTE##NOTE##NOTE##NOTE#
#NOTE#  GROUP  2  #NOTE#
#NOTE##NOTE##NOTE##NOTE#

def random_segment(string, min_length = "N/A = VOID = EMPTY", max_length = "N/A = VOID = EMPTY"):
    """returns a random segment from the string in the first input
       the length of that segment is specified in the other two inputs (it can be random: ("string", 1, 4), or fixated: ("string", 2))"""
    if min_length == "N/A = VOID = EMPTY":
        min_length = random.randint(1, len(string))
    if max_length == "N/A = VOID = EMPTY":
        max_length = min_length
    length = random.randint(min_length, max_length)
    location = random.randint(0, len(string) - length)
    return string[location: location + length]
def random_string(min_length = "N/A = VOID = EMPTY", max_length = "N/A = VOID = EMPTY", type = "alphanumeric"):
    """returns a random (alphanumeric by default) string
       mminimum length can be specified in the first argument, maximum length in the second
       just like in random_segment(), you can use only one integer argument for fixated length
       if no arguments are given, the default minimum length is 1 and default maximum is 256
       if the string declared to the third argument (type) has "alpha" in it, returned string will have alpha characters, if it (also) has "numeric", there will (also possibly) be numbers in the string
       if the string declared to the type also has "lower", there will be no uppercase, if it has "upper", they will be only uppercase"""
    if min_length == "N/A = VOID = EMPTY":
        min_length = random.randint(1, 256)
    if max_length == "N/A = VOID = EMPTY":
        max_length = min_length
    length = random.randint(min_length, max_length)
    possible_letters = ""
    if "alpha" in type:
        if "lower" in type:
            possible_letters += "abcdefghijklmnopqrstuvwxyz"
        elif "upper" in type:
            possible_letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            possible_letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
    if "numeric" in type:
        possible_letters += "1234567890"
    if possible_letters == "":
        possible_letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for count in range(length):
        string += possible_letters[random.randint(0, len(possible_letters) - 1)]
    return(string)


#NOTE##NOTE##NOTE##NOTE#
#NOTE#  GROUP  3  #NOTE#
#NOTE##NOTE##NOTE##NOTE#

def extract_paragraphs(HTML_string):
    """EXPERIMENTAL
    extracts <p>aragraphs from HTML code
    returns a list of paragraph contents"""
    possible, found, filling, paragraph, paragraphs = False, False, False, "", []
    for char in HTML_string:
        if not possible:
            if char == "<":
                possible = True
        elif possible:
            if found:
                if filling:
                    if char == "<":
                        possible, found, filling = False, False, False
                        paragraphs.append(paragraph)
                        paragraph = ""
                    else:
                        paragraph += char
                elif char == ">":
                    filling = True
            elif char == "p":
                found = True
            else:
                possible = False
    return(paragraphs)
