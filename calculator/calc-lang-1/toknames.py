# List of token names in a class for a variable like reference for the names.
# This class is not used by lexer but by the Parser (for better checking)
# it should match with the token names as given in the lexer module
class TokNames:
    NUMBER = 'NUMBER'
    
    ID = "ID"

    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = 'TIMES'
    DIVIDE = 'DIVIDE'
    REMAINDER = 'REMAINDER'
    POWER = 'POWER'

    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    COMMA = 'COMMA'

    ASSIGN = 'ASSIGN'
    PLUS_ASSIGN = 'PLUS_ASSIGN'
    MINUS_ASSIGN = 'MINUS_ASSIGN'
    TIMES_ASSIGN = 'TIMES_ASSIGN'
    DIVIDE_ASSIGN = 'DIVIDE_ASSIGN'
    REMAINDER_ASSIGN = 'REMAINDER_ASSIGN'
    POWER_ASSIGN = 'POWER_ASSIGN'

    EOS = "END_OF_STREAM"


