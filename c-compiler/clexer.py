#!/usr/bin/env python3
"""
A lexer for the complete ANSI C language. Under development.
"""
import ply.lex as lex
import re

class Clexer(object):
    # Build the lexer
    def __init__(self,**kwargs):
        """
        Possible kwargs:
          optimize = 1
          lextab = "lextabname" # creates lextabname.py for faster loading later
          debug = 1
        """
        self.lex = lex.lex(module=self, **kwargs)

        self.newline = re.compile(r"([^\\]?\n|(\\\\)+\n)")

    keywords = {
        "asm"           :"ASM",
        "auto"          :"AUTO",
        "break"         :"BREAK",
        "case"          :"CASE",
        "char"          :"CHAR",
        "const"         :"CONST",
        "continue"      :"CONTINUE",
        "default"       :"DEFAULT",
        "do"            :"DO",
        "double"        :"DOUBLE",
        "else"          :"ELSE",
        "enum"          :"ENUM",
        "extern"        :"EXTERN",
        "float"         :"FLOAT",
        "for"           :"FOR",
        "fortran"       :"FORTRAN",
        "goto"          :"GOTO",
        "if"            :"IF",
        "int"           :"INT",
        "long"          :"LONG",
        "register"      :"REGISTER",
        "return"        :"RETURN",
        "short"         :"SHORT",
        "signed"        :"SIGNED",
        "sizeof"        :"SIZEOF",
        "static"        :"STATIC",
        "struct"        :"STRUCT",
        "switch"        :"SWITCH",
        "typedef"       :"TYPEDEF",
        "union"         :"UNION",
        "unsigned"      :"UNSIGNED",
        "void"          :"VOID",
        "volatile"      :"VOLATILE",
        "while"         :"WHILE",
    }

    # List of token names. This is always required
    tokens = [
        'PREPROCESSOR',
        'ID',
        'INTEGER',
        'REAL',
        'CHR',
        'BADCHR',
        'STRING',

        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'LBRACE',
        'RBRACE',
        'SEMICOLON',
        'COMMA',

        'LINECOMMENT',
        'COMMENT',

        'STAR',
        'DIV',
        'PLUS',
        'MINUS',
        'MOD',

        'ASSIGN',
        'STARASSIGN',
        'DIVASSIGN',
        'PLUSASSIGN',
        'MINUSASSIGN',
        'MODASSIGN',
        'INCREMENT',
        'DECREMENT',

        'DOT',
        'ARROW',

        'LT',
        'LE',
        'EQ',
        'NE',
        'GE',
        'GT',

        'ADDRESSOF',
    ] + list(keywords.values())


    # Regular expression rules for simple tokens
    t_LPAREN        = r'\('
    t_RPAREN        = r'\)'
    t_LBRACKET      = r'\['
    t_RBRACKET      = r'\]'
    t_LBRACE        = r'\{'
    t_RBRACE        = r'\}'
    t_SEMICOLON     = r';'
    t_COMMA         = r','

    t_STAR          = r"\*"
    t_PLUS          = r"\+"
    t_MINUS         = r"-"
    t_DIV           = r"/"
    t_MOD           = r"%"

    t_LT            = r"<"
    t_LE            = r"<="
    t_EQ            = r"=="
    t_NE            = r"!="
    t_GE            = r">="
    t_GT            = r">"

    t_ASSIGN        = r"="
    t_STARASSIGN    = r"\*="
    t_DIVASSIGN     = r"/="
    t_PLUSASSIGN    = r"/="
    t_MINUSASSIGN   = r"/="
    t_MODASSIGN     = r"/="
    t_INCREMENT     = r"\+\+"
    t_DECREMENT     = r"--"

    t_DOT           = r"\."
    t_ARROW         = r"->"

    t_ADDRESSOF     = r"&"

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_PREPROCESSOR(self, t):
        r'[ \t]*\#(\\\n|.)*?\n'
        m = self.newline.findall(t.value)
        t.lexer.lineno += len(m)
        t.value = t.value.strip()
        return t

    def t_COMMENT(self, t):
        r'/\*(.*?|\n)*\*/'
        m = self.newline.findall(t.value)
        t.lexer.lineno += len(m)
        return t

    def t_LINECOMMENT(self, t):
        r'//.*\n'
        m = self.newline.findall(t.value)
        t.lexer.lineno += len(m)
        return t

    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.keywords.get(t.value, 'ID')
        return t

    def t_REAL(self, t):
        r'(\d*\.\d+|\d+\.\d*|\d+)[eE][+-]?\d+|\d+\.|\.\d+'

        return t

    def t_INTEGER(self, t):
        r'0[Xx][0-9a-fA-F]+|\d+'
        if t.value.lower().startswith("0x"):
            t.value = int(t.value, 16)
        elif t.value.startswith("0"):
            t.value = int(t.value, 8)
        else:
            t.value = int(t.value, 10)

        return t

    def t_CHR(self, t):
        r"'(\\['anbvtf]|\\\d{3}|\\[Xx][0-9a-fA-F]{2}|.{1})'"
        return t

    def t_BADCHR(self, t):
        r"'.*?'"
        return t

    def t_STRING(self,t):
        r'"(\\"|\\\n|.)*?"'
        m = self.newline.findall(t.value)
        t.lexer.lineno += len(m)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '{}'".format(t.value[0]))
        t.lexer.skip(1)

    # Test output
    def test(self,data):
        self.lex.input(data)
        while True:
             tok = self.lex.token()
             if not tok: 
                 break
             print(tok)

    def autotest(self):
        lex.runmain()

if __name__ == '__main__':
    # Build the lexer and try it out
    m = Clexer(debug=1)
    m.autotest()
    #m.test("3 + 4")     # Test it
    #m.test("\n3 + 4")     # Test it


