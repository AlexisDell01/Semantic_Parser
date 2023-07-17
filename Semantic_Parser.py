first_follows = {
    ('PROGRAMA', 'programa'): [['programa', 'id', ';', 'CUERPO', '.']],
    ('CUERPO', 'variable'): [["DECLARACIONES", "PRINCIPAL"]],
    ('CUERPO', '{'): [['PRINCIPAL']],
    ('DECLARACIONES', 'variable'): [['variable', "LISTAIDS", ':', "TIPOS", ';', "AUX1"]],
    ('AUX1', 'id'): [["LISTAIDS", ':', "TIPOS", ';', "AUX1"]],
    ('AUX1', '{'): [['']],
    ('LISTAIDS', 'id'): [['id', "AUX2"]],
    ('AUX2', ','): [[',',"AUX2"]],
    ('AUX2', ':'): [['']],
    ("TIPOS", 'enteros'): [["ESTANDAR"]],
    ("TIPOS", 'real'): [["ESTANDAR"]],
    ("TIPOS", 'cadena'): [["ESTANDAR"]],
    ("TIPOS", 'byte'): [["ESTANDAR"]],
    ("TIPOS", 'caracter'): [["ESTANDAR"]],
    ("TIPOS", 'booleano'): [["ESTANDAR"]],
    ("TIPOS", 'arreglo'): [["VECTORES"]],
    ("ESTANDAR", 'enteros'): [['enteros']],
    ("ESTANDAR", 'real'): [['real']],
    ("ESTANDAR", 'cadena'): [['cadena']],
    ("ESTANDAR", 'byte'): [['byte']],
    ("ESTANDAR", 'caracter'): [['caracter']],
    ("ESTANDAR", 'booleano'): [['booleano']],
    ("PRINCIPAL", '{'): [['{', "ESTATUTOS", '}']],
    ("ESTATUTOS", 'id'): [["ESTATUTO", ';', "AUX3"]],
    ("ESTATUTOS", 'para'): [["ESTATUTO", ';', "AUX3"]],
    ("ESTATUTOS", 'mientras'): [["ESTATUTO", ';', "AUX3"]],
    ("ESTATUTOS", 'repetir'): [["ESTATUTO", ';', "AUX3"]],
    ("ESTATUTOS", 'leer'): [["ESTATUTO", ';', "AUX3"]],
    ("ESTATUTOS", 'escribir'): [["ESTATUTO", ';', "AUX3"]],
    ("ESTATUTOS", 'si'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'id'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'para'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'mientras'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'repetir'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'leer'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'escribir'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", 'si'): [["ESTATUTO", ';', "AUX3"]],
    ("AUX3", '}'): [['']],
    ("AUX3", 'hasta'): [['']],
    ("VECTORES", 'arreglo'): [['arreglo', '[', 'cte.entera', '..', 'cte.entera', "AUX4", ']','de',"ESTANDAR"]],
    ("AUX4", ','): [[',','cte.entera',':','cte.entera',"AUX4"]],
    ("AUX4", ']'): [['']],
    ("ESTATUTO", 'id'): [['ASIGNACION']],
    ("ESTATUTO", 'para'): [['CICLO-FOR']],
    ("ESTATUTO", 'mientras'): [['CICLO-WHILE']],
    ("ESTATUTO", 'repetir'): [['CICLO-REPETIR']],
    ("ESTATUTO", 'leer'): [['ENTRADA']],
    ("ESTATUTO", 'escribir'): [['SALIDA']],
    ("ESTATUTO", 'si'): [['IF']],
    ("ASIGNACION", 'id'): [["VARIABLE", '=', "EXPRESION"]],
    ("VARIABLE", 'id'): [['id', "AUX5"]],
    ("AUX5", '['): [['[',"EXPRESION", "AUX6",']']],
    ("AUX5", '='): [['']],
    ("AUX5", ','): [['']],
    ("AUX5", ')'): [['']],
    ("AUX5", '*'): [['']],
    ("AUX5", '/'): [['']],
    ("AUX5", 'division'): [['']],
    ("AUX5", 'modulo'): [['']],
    ("AUX5", 'y'): [['']],
    ("AUX5", '+'): [['']],
    ("AUX5", '-'): [['']],
    ("AUX5", 'o'): [['']],
    ("AUX5", '<'): [['']],
    ("AUX5", '>'): [['']],
    ("AUX5", '<='): [['']],
    ("AUX5", '>='): [['']],
    ("AUX5", '<>'): [['']],
    ("AUX5", ';'): [['']],
    ("AUX5", 'do'): [['']],
    ("AUX5", 'hacer'): [['']],
    ("AUX5", 'entonces'): [['']],
    ("AUX5", 'para'): [['']],
    ("AUX5", ']'): [['']],
    ("AUX6", ','): [[',',"EXPRESION", "AUX6"]],
    ("AUX6", ']'): [['']],
    ("CICLO-REPETIR", 'repetir'): [['repetir', "ESTATUTOS", 'hasta', "EXPRESION"]],
    ("CICLO-FOR", 'para'): [['para', "CONTADOR", 'do', '{', "ESTATUTOS", '}']],
    ("CONTADOR", 'id'): [['id', '=', "EXPRESION", 'para', "EXPRESION"]],
    ("CICLO-WHILE", 'mientras'): [['mientras', "EXPRESION", 'hacer', '{', "ESTATUTOS", '}']],
    ("ENTRADA", 'leer'): [['leer', '(', "VARIABLE", "AUX7", ')']],
    ("AUX7", ','): [[',',"VARIABLE", "AUX7"]],
    ("AUX7", ')'): [['']],
    ("SALIDA", 'escribir'): [['escribir', '(', "EXPRESION", "AUX8", ')']],
    ("AUX8", ','): [[',', "EXPRESION", "AUX8"]],
    ("AUX8", ')'): [['']],
    ("IF", 'si'): [['si', "EXPRESION", 'entonces', '{', "ESTATUTOS", '}', "AUX9",'fin_sino']],
    ("AUX9", 'sino'): [['sino', '{', "ESTATUTOS", '}']],
    ("AUX9", 'fin_sino'): [['']],
    ("EXPRESION", '('): [["EXP", "AUX10"]],
    ("EXPRESION", 'id'): [["EXP", "AUX10"]],
    ("EXPRESION", 'verdadero'): [["EXP", "AUX10"]],
    ("EXPRESION", 'falso'): [["EXP", "AUX10"]],
    ("EXPRESION", 'cte.entera'): [["EXP", "AUX10"]],
    ("EXPRESION", 'cte.real'): [["EXP", "AUX10"]],
    ("EXPRESION", 'cte.cadena'): [["EXP", "AUX10"]],
    ("EXPRESION", 'no'): [["EXP", "AUX10"]],
    ("AUX10", '='): [["RELACIONAL", "EXP"]],
    ("AUX10", '<'): [["RELACIONAL", "EXP"]],
    ("AUX10", '>'): [["RELACIONAL", "EXP"]],
    ("AUX10", '<='): [["RELACIONAL", "EXP"]],
    ("AUX10", '>='): [["RELACIONAL", "EXP"]],
    ("AUX10", '<>'): [["RELACIONAL", "EXP"]],
    ("AUX10", ','): [[""]],
    ("AUX10", ';'): [[""]],
    ("AUX10", 'do'): [[""]],
    ("AUX10", 'hacer'): [[""]],
    ("AUX10", 'entonces'): [[""]],
    ("AUX10", ')'): [[""]],
    ("AUX10", 'para'): [[""]],
    ("AUX10", ']'): [[""]],
    ("EXP", '('): [["TERMINO", "AUX11"]],
    ("EXP", 'id'): [["TERMINO", "AUX11"]],
    ("EXP", 'verdadero'): [["TERMINO", "AUX11"]],
    ("EXP", 'falso'): [["TERMINO", "AUX11"]],
    ("EXP", 'cte.entera'): [["TERMINO", "AUX11"]],
    ("EXP", 'cte.real'): [["TERMINO", "AUX11"]],
    ("EXP", 'cte.cadena'): [["TERMINO", "AUX11"]],
    ("EXP", 'no'): [["TERMINO", "AUX11"]],
    ("AUX11", '+'): [['+', "TERMINO", "AUX11"]],
    ("AUX11", '-'): [['-', "TERMINO", "AUX11"]],
    ("AUX11", 'o'): [['o', "TERMINO", "AUX11"]],
    ("AUX11", '='): [['']],
    ("AUX11", '<'): [['']],
    ("AUX11", '>'): [['']],
    ("AUX11", '<='): [['']],
    ("AUX11", '>='): [['']],
    ("AUX11", '<>'): [['']],
    ("AUX11", ','): [['']],
    ("AUX11", ';'): [['']],
    ("AUX11", 'do'): [['']],
    ("AUX11", 'hacer'): [['']],
    ("AUX11", 'entonces'): [['']],
    ("AUX11", ')'): [['']],
    ("AUX11", 'para'): [['']],
    ("AUX11", ']'): [['']],
    ("RELACIONAL", '='): [['=']],
    ("RELACIONAL", '<'): [['<']],
    ("RELACIONAL", '>'): [['>']],
    ("RELACIONAL", '<='): [['<=']],
    ("RELACIONAL", '>='): [['>=']],
    ("RELACIONAL", '<>'): [['<>']],
    ("TERMINO", '('): [["FACTOR", "AUX12"]],
    ("TERMINO", 'id'): [["FACTOR", "AUX12"]],
    ("TERMINO", 'verdadero'): [["FACTOR", "AUX12"]],
    ("TERMINO", 'cte.entera'): [["FACTOR", "AUX12"]],
    ("TERMINO", 'falso'): [["FACTOR", "AUX12"]],
    ("TERMINO", 'cte.real'): [["FACTOR", "AUX12"]],
    ("TERMINO", 'cte.cadena'): [["FACTOR", "AUX12"]],
    ("TERMINO", 'no'): [["FACTOR", "AUX12"]],
    ("AUX12", '*'): [['*', "FACTOR", "AUX12"]],
    ("AUX12", '/'): [['/',"FACTOR", "AUX12"]],
    ("AUX12", 'division'): [['division',"FACTOR", "AUX12"]],
    ("AUX12", 'modulo'): [['modulo',"FACTOR", "AUX12"]],
    ("AUX12", 'y'): [['y',"FACTOR", "AUX12"]],
    ("AUX12", '+'): [[""]],
    ("AUX12", '-'): [[""]],
    ("AUX12", 'o'): [[""]],
    ("AUX12", '='): [[""]],
    ("AUX12", '<>'): [[""]],
    ("AUX12", '<='): [[""]],
    ("AUX12", '>='): [[""]],
    ("AUX12", '<'): [[""]],
    ("AUX12", '>'): [[""]],
    ("AUX12", ','): [[""]],
    ("AUX12", ';'): [[""]],
    ("AUX12", 'do'): [[""]],
    ("AUX12", 'hacer'): [[""]],
    ("AUX12", 'entonces'): [[""]],
    ("AUX12", ')'): [[""]],
    ("AUX12", 'para'): [[""]],
    ("AUX12", ']'): [[""]],
    ("FACTOR", '('): [['(',"EXPRESION",')']],
    ("FACTOR", 'id'): [["VARIABLE"]],
    ("FACTOR", 'verdadero'): [["verdadero"]],
    ("FACTOR", 'cte.entera'): [["cte.entera"]],
    ("FACTOR", 'falso'): [["falso"]],
    ("FACTOR", 'cte.real'): [["cte.real"]],
    ("FACTOR", 'cte.cadena'): [["cte.cadena"]],
    ("FACTOR", 'no'): [['no',"EXPRESION"]],
}


syntax = {
    "PROGRAMA": [['programa', 'id', ';', "CUERPO", "."]],
    "CUERPO": [["DECLARACIONES", "PRINCIPAL"], ['PRINCIPAL']],
    "DECLARACIONES": [['variable', "LISTAIDS", ':', "TIPOS", ';', "AUX1"]],
    "AUX1": [["LISTAIDS", ':', "TIPOS", ';', "AUX1"], ['']],
    "LISTAIDS": [['id', "AUX2"]],
    "AUX2": [[',',"AUX2"], ['']],
    "TIPOS": [["ESTANDAR"], ["VECTORES"]],
    "ESTANDAR": [['enteros'], ['real'], ['cadena'], ['byte'], ['caracter'], ['booleano']],
    "PRINCIPAL": [['{', "ESTATUTOS", '}']],
    "ESTATUTOS": [["ESTATUTO", ';', "AUX3"]],
    "AUX3": [["ESTATUTO", ';', "AUX3"], ['']],
    "VECTORES": [['arreglo', '[', 'cte.entera', '..', 'cte.entera', "AUX4", ']','de',"ESTANDAR"]],
    "AUX4": [[',','cte.entera',':','cte.entera',"AUX4"], ['']],
    "ESTATUTO": [["ASIGNACION"], ["CICLO-FOR"], ["CICLO-WHILE"], ["CICLO-REPETIR"], ["ENTRADA"], ["SALIDA"], ["IF"]],
    "ASIGNACION": [["VARIABLE", '=', "EXPRESION"]],
    "VARIABLE": [['id', "AUX5"]],
    "AUX5": [['[',"EXPRESION", "AUX6",']'], ['']],
    "AUX6": [[',',"EXPRESION", "AUX6"], ['']],
    "CICLO-REPETIR": [['repetir', "ESTATUTOS", 'hasta', "EXPRESION"]],
    "CICLO-FOR": [['para', "CONTADOR", 'do', '{', "ESTATUTOS", '}']],
    "CONTADOR": [['id', '=', "EXPRESION", 'para', "EXPRESION"]],
    "CICLO-WHILE": [['mientras', "EXPRESION", 'hacer', '{', "ESTATUTOS", '}']],
    "ENTRADA": [['leer', '(', "VARIABLE", "AUX7", ')']],
    "AUX7": [[',',"VARIABLE", "AUX7"],['']],
    "SALIDA": [['escribir', '(', "EXPRESION", "AUX8", ')']],
    "AUX8": [[',', "EXPRESION", "AUX8"], ['']],
    "IF": [['si', "EXPRESION", 'entonces', '{', "ESTATUTOS", '}', "AUX9",'fin_sino']],
    "AUX9": [['sino', '{', "ESTATUTOS", '}'], ['']],
    "EXPRESION": [["EXP", "AUX10"]],
    "AUX10": [["RELACIONAL", "EXP"], ['']],
    "EXP": [["TERMINO", "AUX11"]],
    "AUX11": [['+', "TERMINO", "AUX11"],['-', "TERMINO", "AUX11"],['o', "TERMINO", "AUX11"],['']],
    "RELACIONAL": [['='],['<'],['>'],['<='],['>='],['<>']],
    "TERMINO": [["FACTOR", "AUX12"]],
    "AUX12": [['*', "FACTOR", "AUX12"],['/', "FACTOR", "AUX12"],['division', "FACTOR", "AUX12"],['modulo', "FACTOR", "AUX12"],['y', "FACTOR", "AUX12"], ['']],
    "FACTOR": [['(',"EXPRESION",')'], ["VARIABLE"], ['verdadero'], ['falso'], ['cte.entera'],['cte.real'],['cte.cadena'],['no',"EXPRESION"]]
}



def analizar_sintacticamente(cadena):
    stack = ['$', 'PROGRAMA']
    indice = 0
    
    while stack:
        simbolo_actual = stack[-1]
        if indice >= len(cadena):
            token_actual = '$'
        else:
            token_actual = cadena[indice]
        
        print('Stack:', stack)
        print('Current Token:', token_actual)
        
        if simbolo_actual == token_actual:
            stack.pop()
            if token_actual != '$':
                indice += 1
        elif simbolo_actual in syntax:
            produccion = first_follows.get((simbolo_actual, token_actual))
            if produccion:
                stack.pop()
                if produccion[0] != ['']:
                    stack.extend(reversed(produccion[0]))
            else:
                print("Syntax error: No production found in the prediction table for the current symbol!")
                print("Current Symbol:", simbolo_actual)
                print("Current Token:", token_actual)
                
                return False
        else:
            print("Syntax error: Current symbol does not match stack")
            print("Current Symbol:", simbolo_actual)
            print("Current Token:", token_actual)
            return False
    
    if indice == len(cadena):
        print("Successful Parser!")
        return True
    else:
        print("Syntax error: End of input string reached but stack is not empty")
        return False
    

lecture = ['programa', 'id', ';', '{', 'id','=', 'cte.cadena', ';', '}', '.']
lecture = ['programa', 'id', ';', '{', 'si', '(', 'verdadero', ')', 'entonces', '{', 'id', '=', 'cte.real', ';', '}', 'sino', '{', 'id', '=', 'cte.real',  ';', '}', 'fin_sino',';', '}', '.']

analizar_sintacticamente(lecture)

