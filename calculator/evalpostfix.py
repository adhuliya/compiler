#!/usr/bin/env python3

"""
This program takes as input a space separated list of numbers (interger assumed) 
and operator plus (+), minus (-) and multiply (*) in a postfix form 
and prints out the result.
"""


def tolist (pfixexpr):
    """
    Conver a comma separated input into a list of strings
    """
    pfixlist = []
    elements = pfixexpr.split(" ")
    for element in elements:
        elem = element.strip()
        if elem:
            pfixlist.append (elem)
    return pfixlist

def evalpfix (pfixlist):
    """
    Evaluates a postfix expressiong using a stack.
    """
    stack = []

    for elem in pfixlist:
        if elem == '+':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append (a + b)
        elif elem == '-':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append (a - b)
        elif elem == '*':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append (a * b)
        else:
            stack.append (elem)

    return int(stack.pop ())


if __name__ == '__main__':
    pfixexpr = input()
    pfixlist = tolist (pfixexpr)

    result = evalpfix (pfixlist)
    print ("Result = ", result)


