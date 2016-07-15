"""
The is the parser of calclang. It converts a line of calclang into
a format understood by the CalcVM (a virtual machine for calculator)
"""
def line(tokstream):
    """
    'line' is the start symbol of the grammar
    """
    tok = tokstream.nextToken()


    print (type(tok.type))
    print (tok.type == 'ID')
    print (tok.value)
    print (dir(tok))



def parse(inptline):
    tokstream = Tokenizer(inptline)

    # start parsing from the top symbol
    line(tokstream)

if __name__ == '__main__':
    parse("x = 10")

