
        'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

        # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
        'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
        'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

        # Increment/decrement (++,--)
        'INCREMENT', 'DECREMENT',

        # Delimeters ( ) [ ] { } , . ; :
        'LPAREN', 'RPAREN',
        'LBRACKET', 'RBRACKET',
        'LBRACE', 'RBRACE',
        'COMMA', 'PERIOD', 'SEMI', 'COLON',

    ]
    t_ignore = ' \t\n'
    
    # Operators
    t_PLUS             = r'\+'
    t_MINUS            = r'-'
    t_TIMES            = r'\*'
    t_DIVIDE           = r'/'
    t_MODULO           = r'%'
    t_OR               = r'\|'
    t_AND              = r'&'
    t_NOT              = r'~'
    t_XOR              = r'\^'
    t_LSHIFT           = r'<<'
    t_RSHIFT           = r'>>'
    t_LOR              = r'\|\|'
    t_LAND             = r'&&'
    t_LNOT             = r'!'
    t_LT               = r'<'
    t_GT               = r'>'
    t_LE               = r'<='
    t_GE               = r'>='
    t_EQ               = r'=='
    t_NE               = r'!='

    # Assignment operators

    t_EQUALS           = r'='
    t_TIMESEQUAL       = r'\*='
    t_DIVEQUAL         = r'/='
    t_MODEQUAL         = r'%='
    t_PLUSEQUAL        = r'\+='
    t_MINUSEQUAL       = r'-='
    t_LSHIFTEQUAL      = r'<<='
    t_RSHIFTEQUAL      = r'>>='
    t_ANDEQUAL         = r'&='
    t_OREQUAL          = r'\|='
    t_XOREQUAL         = r'\^='

    # Increment/decrement
    t_INCREMENT        = r'\+\+'
    t_DECREMENT        = r'--'

    # Delimeters
    t_LPAREN           = r'\('
    t_RPAREN           = r'\)'
    t_LBRACKET         = r'\['
    t_RBRACKET         = r'\]'
    t_LBRACE           = r'\{'
    t_RBRACE           = r'\}'
    t_COMMA            = r','
    t_PERIOD           = r'\.'
    t_SEMI             = r';'
    t_COLON            = r':'

    # Identifiers
    t_NAME = r'[A-Za-z_][A-Za-z0-9_]*'

    # Integer literal
    t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

    # Floating literal
    t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

    # String literal
    t_STRING = r'\"([^\\\n]|(\\.))*?\"'

    # Character constant 'c' or L'c'
    t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''


# Error handling rule
    def t_error(t):
        print("Caracter Ilegal '%s'" % t.value[0])
        t.lexer.skip(1)            
    lex.lex()
    lex.input(caracteres)
    while True:
        tok = lex.token()
        if not tok: break
        if (str(tok.value)== "escribir" or str(tok.value)== "leer" or str(tok.value)=="si" or str(tok.value)=="mientras" or str(tok.value)=="si no" or str(tok.value)=="para" or str(tok.value)=="hasta"):
            print(str(tok.value) + " --> " + "Palabra Reservada")
        else:
            print(str(tok.value) + " --> " + str(tok.type))
        
        

def main ():
    #cargarArchivo("datos.txt")
    archivo = open("datos.txt")
    caracteres = archivo.read()
    archivo.close()
    analisis_lex(caracteres)
   
    
if __name__ == "__main__":
    main()
