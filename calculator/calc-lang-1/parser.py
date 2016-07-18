"""
The is the parser of calclang. It converts a line of calclang into
a format understood by the CalcVM (a virtual machine for calculator).
It is denoted here as the 'target program'
"""

"""
The target program is put into the 'targetprogram' list
"""
import bufferedlexer as bufflex
from toknames import TokNames

class Parser:
    def __init__(self):
        self.targetprogram = []
        self.tokstream = None
        self.currtok = None

        self.assigndict = { 
                TokNames.ASSIGN:"=",
                TokNames.PLUS_ASSIGN:"+=",
                TokNames.MINUS_ASSIGN:"-=", 
                TokNames.TIMES_ASSIGN:"*=",
                TokNames.DIVIDE_ASSIGN:"/=", 
                TokNames.REMAINDER_ASSIGN:"%=",
                TokNames.POWER_ASSIGN:"**="
           }


    """
    Returns the targetprogram and an error (if found else None)
    """
    def parse(self, inptline):
        self.targetprogram = []
        self.tokstream = bufflex.Lexer(inptline)

        # start parsing from the top symbol
        err = self.line()
        if err != None: return None, err

        return self.targetprogram, None


    def line(self):
        """
        'line' is the start symbol of the grammar
        """
        self.nextToken()

        if self.currtok.type == TokNames.ID:
            err = self.match([TokNames.ID]);
            if err: return err
            self.nextToken()

            ok, err = self.assign(); # ok if it is indeed assignment stmt
            if err: return err

            if not ok:
                self.prevToken()
                self.prevToken()
                self.nextToken()
                return self.expr()
            else:
                return None

        else:
            return self.expr()


    def assign(self):
        ok = True # assume that it is an assign stmt
        notok = False # it is not an assign stmt

        if self.currtok == None:
            return ok, None

        if self.currtok.type in self.assigndict:
            toktype = self.currtok.type

            err = self.match(self.assigndict)
            if err: return ok, err

            self.prevToken()
            self.prevToken()
            self.nextToken()
            self.targetprogram.append(self.currtok.value)
            self.nextToken() 
            self.nextToken()

            err = self.expr()
            if err: return ok, err

            self.targetprogram.append(self.assigndict[toktype])

            return ok, None
        else:
            return notok, None


    def expr(self):
        err = self.term()
        if err: return err

        err = self.exprRest()
        if err: return err

        return None


    def exprRest(self):
        if self.currtok == None:
            return None

        if self.currtok.type == TokNames.PLUS:
            err = self.match([TokNames.PLUS])
            if err: return err

            self.nextToken()
            err = self.term()
            if err: return err

            self.targetprogram.append("+")

            err = self.exprRest()
            if err: return err

            return None

        elif self.currtok.type == TokNames.MINUS:
            err = self.match([TokNames.MINUS])
            if err: return err

            self.nextToken()
            err = self.term()
            if err: return err

            self.targetprogram.append("-")

            err = self.exprRest()
            if err: return err

            return None
        else:
            return None


    def term(self):
        err = self.power()
        if err: return err

        err = self.termRest()
        if err: return err

        return None


    def termRest(self):
        if self.currtok == None:
            return None

        if self.currtok.type == TokNames.TIMES:
            err = self.match([TokNames.TIMES])
            if err: return err

            self.nextToken()
            err = self.power()
            if err: return err

            self.targetprogram.append("*")

            err = self.termRest()
            if err: return err

            return None

        if self.currtok.type == TokNames.DIVIDE:
            err = self.match([TokNames.DIVIDE])
            if err: return err

            self.nextToken()
            err = self.power()
            if err: return err

            self.targetprogram.append("/")

            err = self.termRest()
            if err: return err

            return None

        if self.currtok.type == TokNames.REMAINDER:
            err = self.match([TokNames.REMAINDER])
            if err: return err

            self.nextToken()
            err = self.power()
            if err: return err

            self.targetprogram.append("%")

            err = self.termRest()
            if err: return err

            return None
        else:
            return None


    def power(self):
        err = self.factor()
        if err: return err

        err = self.powerRest()
        if err: return err

        return None


    def powerRest(self):
        if self.currtok == None: return None

        if self.currtok.type == TokNames.POWER:
            err = self.match([TokNames.POWER])
            if err: return err

            self.nextToken()
            err = self.power()
            if err: return err

            self.targetprogram.append("**")

        else:
            return None


    def factor(self):
        if self.currtok == None: 
            return "factor: Expecting factor got None"

        if self.currtok.type == TokNames.NUMBER:
            self.targetprogram.append(self.currtok.value)
            self.nextToken()

            return None

        elif self.currtok.type == TokNames.LPAREN:
            self.nextToken()

            err = self.expr()
            if err: return err

            err = self.match(TokNames.RPAREN)
            if err: return err
            self.nextToken()

        elif self.currtok.type == TokNames.ID:
            err = self.named()
            if err: return err

            return None
        else:
            return "factor: Expecting NUMBER, LPAREN or ID : got : " + self.currtok


    def named(self):
        if self.currtok == None: 
            return "named: Expecting Name got None"

        if self.currtok.type == TokNames.ID:
            name = self.currtok.value

            err = self.match([TokNames.ID])
            if err: return err
            self.nextToken()

            err = self.parens()
            if err: return err

            self.targetprogram.append(name)

        else:
            return "named: Expecting an ID got " + self.currtok


    def parens(self):
        if self.currtok == None:
            return None

        if self.currtok.type == TokNames.LPAREN:
            self.targetprogram.append("(")
            
            self.nextToken()
            err = self.args()
            if err: return err

            err = self.match(TokNames.RPAREN)
            if err: return err
            self.targetprogram.append(")")
            self.nextToken()

        else:
            return None


    def args(self):
        if self.currtok == None: return None

        if self.currtok.type == TokNames.RPAREN:
            return None
        else:
            err = self.expr()
            if err: return err

            err = self.params()
            if err: return err

            return None


    def params(self):
        if self.currtok.type == TokNames.COMMA:
            self.nextToken()

            err = self.expr()
            if err: return err

            err = params()
            if err: return err

        else:
            return None


    def match(self, toknames):
        if self.currtok.type in toknames:
            return None
        else:
            return ("Unkown token :" + self.currtok + 
                    ". Expected token type(s):" + tokname)

    def nextToken(self):
        self.currtok = self.tokstream.nextToken()

    def prevToken(self):
        self.tokstream.prevToken()


