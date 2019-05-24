from Nodo import Nodo
import ply.yacc as yacc
from tokrules import tokens
import tokrules 


index = 0

def p_iniciando(p):
    'inicio : init'
    p[0]=p[1]

def p_contenido(p):
    'init : ACORCH cnt CCORCH'
    p[0]=p[2]

def p_lista(p):
    '''cnt : cnt COMA STRING DSPTS valor
           | STRING DSPTS valor'''
    if (len(p)==6):
        print "es 6"
        p[0] = p[1]
        p[3] = Nodo(p[3],"",p.lineno(3),p.lexpos(3),index)
        if (p[5].getNombre() == '#'):
            p[3].append(p[5])
        else:
            p[3].setValor(p[5].getValor())
        p[0].append(p[3])
    elif (len(p)==4):    
        print "es 4"
        p[0] = Nodo("#","#",0,0,index)
        global index
        index = index + 1
        if (p[3].getNombre() == '#'):
            print " es #"
            p[1] = Nodo(p[1],"",p.lineno(1),p.lexpos(1),index)
            global index
            index = index + 1
            p[1].append(p[3])
        else:
            print "es otra cosa"
            p[1] = Nodo(p[1],"",p.lineno(1),p.lexpos(1),index)
            global index
            index = index + 1
            p[1].setValor(p[3].getValor())
        p[0].append(p[1])

def p_valorVar(p):
    'valor : VAR'
    p[0]= Nodo("id",p[1],p.lineno(1),p.lexpos(1),index)
    global index
    index = index + 1
    #p[0].printNodo()

def p_valorNumber(p):
    'valor : NUMBER'
    p[0]= Nodo("number",str(p[1]),p.lineno(1),p.lexpos(1),index)
    global index
    index = index + 1
    #p[0].printNodo()

def p_valorString(p):
    'valor : STRING'
    p[0]= Nodo("string",p[1],p.lineno(1),p.lexpos(1),index)
    global index
    index = index + 1
    #p[0].printNodo()

def p_valorInit(p):
    'valor : init'
    p[0] = p[1]
    #p[0].printNodo()

def p_error(subexpr):
    raise Exception("Syntax error.")
