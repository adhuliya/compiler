import ply.lex as lex

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

    reserved = {
            'int':'INT'
            }

    # List of token names.   This is always required
    tokens = (
        'ID',
        'LBRACE',
        'RBRACE',
        'LPAREN',
        'RPAREN',
        'STRING',
        'SEMICOLON',
    ) + tuple(reserved.values())


    # Regular expression rules for simple tokens
    t_LBRACE    = r'\{'
    t_RBRACE    = r'\}'
    t_SEMICOLON  = r';'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_STRING(self,t):
        r'"(.*|.*(\\")|.*(\\\n))*"' # TODO doesnot handle '\"<cr>'
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Test it output
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
