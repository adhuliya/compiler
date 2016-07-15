#!/usr/bin/env python3
import unittest
import lexer as lex

class TestingClass(unittest.TestCase):
    def test_tokenize(self):
        """
        It tests the calclex.tokenize function in the calclex module.
        """
        testcases = {
                ".32.43 1.23 3.":
                ('LexToken(NUMBER,0.32,1,0), LexToken(NUMBER,0.43,1,3)'
                 ', LexToken(NUMBER,1.23,1,7), LexToken(NUMBER,3.0,1,12)'),
                "x**=abc+sum(max(a,b))":
                ("LexToken(ID,'x',1,0), LexToken(POWER_ASSIGN,'**=',1,1)"
                 ", LexToken(ID,'abc',1,4), LexToken(PLUS,'+',1,7)"
                 ", LexToken(ID,'sum',1,8), LexToken(LPAREN,'(',1,11)"
                 ", LexToken(ID,'max',1,12), LexToken(LPAREN,'(',1,15)"
                 ", LexToken(ID,'a',1,16), LexToken(COMMA,',',1,17)"
                 ", LexToken(ID,'b',1,18), LexToken(RPAREN,')',1,19)"
                 ", LexToken(RPAREN,')',1,20)")}

        # each token has (type, value, lineno, lexpos)
        for key, val in testcases.items():
            x = []
            for tok in lex.tokenize(key):
                x.append(str(tok))

            output = ", ".join(x)

            self.assertTrue(output == val)


if __name__ == "__main__":
    unittest.main()

