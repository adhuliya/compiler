#!/usr/bin/env python3

"""
This program an infix expression into a postfix expression using a syntax
directed translation scheme (i.e. with semantic actions). Currently no
brackets.

The input is considered to be a space separated expression like (of single digits)
9 + 4 - 1

Grammar is:
expr ==> expr + term | expr - term | term
term ==> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

Left factoring:
expr ==> term rest
rest ==> + term rest | - term rest | epsilon
term ==> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

Inserting Semantic Actions:
expr ==> term rest | epsilon
rest ==> + term {print ('+')} rest | - term {print ('-')} rest | epsilon
term ==> 0 {print ('0')} | 1 {print ('1')} | and so on...
""" 
import evalpostfix as ep

token = ""
tokgen = None
postfixlist = []
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def tokengenerator (toklist):
    for tok in toklist:
        yield tok

def match (t):
    global token, tokgen
    if token == t:
        token = next (tokgen)
    else:
        print ("Parsing error with token '{}'".format (token))

def expr ():
    global token
    if token in digits:
        term (); rest ();
    #else epsilon production

def rest () :
    global token
    if token == '+':
        match ('+'); term (); postfixlist.append ('+'); rest ();
    elif token == '-':
        match ('-'); term (); postfixlist.append ('-'); rest ();
    #else epsilon production
    
def term ():
    global token
    if token in digits:
        postfixlist.append (token); match (token); 

def formatproper (line):
    words = line.split ()
    line = "".join (words)
    return line


def compile (line):
    line = formatproper (line)

    toklist = list (line + '$')
    global tokgen
    tokgen = tokengenerator (toklist)

    global token
    token = next (tokgen)
    expr ()

def main ():
    global token, postfixlist, tokgen
    while True:
        token = tokgen = None
        postfixlist = []

        line = input ()
        if (not line.strip() or line.strip() == 'quit' or
           line.strip() == 'exit'):
            break
        compile (line)
        #print ("Postfix expr = ", postfixlist)
        result = ep.evalpfix (postfixlist)
        print (result)

if __name__ == '__main__':
    main ()



