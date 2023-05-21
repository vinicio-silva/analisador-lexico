from asyncio.windows_events import NULL
import string

TABELA_SIMBOLO = open("tabela-simbolo.txt", "r+")
LETRA_LOWER = list(string.ascii_lowercase)
LETRA_UPPER = list(string.ascii_uppercase)
NUMBER = [str(num) for num in range(9)]
CHAR_RESERVED = ['a', 'c', 'e', 'f', 'i', 'r', 's']
ID = LETRA_UPPER + LETRA_LOWER + NUMBER + ['_']

def addTable(char, table):   # Função para inserir na tabela de simbolos
    nro_elem = 1
    table.seek(0, 0)
    for linha in table:
        if (str(char+'\n')) == linha or str(char) == linha:
            return nro_elem
        nro_elem += 1

    table.writelines(char+"\n")
    return nro_elem
def getToken(file, token):
    estado = 'A'
    coluna = 0
    linha = 1
    look_ahead = False
    nro_token = 1
    strAux = ''
    
    while 1:
        if look_ahead is False:
            char = file.read(1)
            coluna +=1
        strAux = strAux + str(char)
        look_ahead = False
        
        #### Estado Inicial ####
        
        if estado == 'A':
            if char == 'a':
                estado = 'B'

            elif char == 'c':
                estado = 'D'

            elif char == 'e':
                estado = 'E'
                
            elif char == 'f':
                estado = 'F'
            
            elif char == 'i':
                estado = 'G'
            
            elif char == 'r':
                estado = 'H'

            elif char == 's':
                estado = 'I'
            
            elif char == '<':
                estado = 'J'
            
            elif char == '-':
                if nro_token == token:
                    return ('Operador Aritimético', '-', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
            
            elif char == '+':
                if nro_token == token:
                    return ('Operador Aritimético', '+', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
            
            elif char == '/': ## <- menos esse 
                estado = 'N'
            
            elif char == '*':
                if nro_token == token:
                    return ('Operador Aritimético', '*', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'

            elif char == '^':
                if nro_token == token:
                    return ('Operador Aritimético', '^', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 

            elif char == '=':
                estado = 'Q'

            elif char == '>':
                estado = 'R'
            
            elif char == '.':
                estado = 'ERR'
            

            elif char == ':':
                if nro_token == token:
                    return (':', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 

            elif char == ',':
                if nro_token == token:
                    return (',', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
            
            elif char == ';':
                if nro_token == token:
                    return (';', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 

            elif char == '(':
                if nro_token == token:
                    return ('(', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
            
            elif char == ')':
                if nro_token == token:
                    return (')', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'

            elif char == '{':         
                if nro_token == token:
                    return ('{', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 

            elif char == '}':
                if nro_token == token:
                    return ('}', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
            
            elif char in NUMBER:
                estado = 'Z'

            elif char == ' ' or char == '\n' or char == '\t':
                estado = 'AB'
            
            elif char == "'":
                estado = 'AA'

            elif char in ID:
                estado = 'C'                
                
            else:
                estado = 'ERR'
                
        ############ ESTADO B #############
           
        elif estado == 'B':
            if char == 't':
                estado = 'AD'         
            else:
                estado = 'C'
                
        ############ ESTADO C #############
            
        elif estado == 'C':
            if char in ID:
                estado = 'C'
            else:
                if nro_token == token:
                    nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                    return ('ID', nro_elem, (linha, coluna))
                else:
                    nro_token +=1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True

        ########### ESTADO D ##############
            
        elif estado == 'D':
            if char == 'h':
                estado = 'AE'
            else:
                estado = 'C'
                
            
        ############ ESTADO E #############
            
        elif estado == 'E':
            if char == 'n':
                estado = 'AF'          
            else:
                estado = 'C'
                look_ahead = True
                
        ############ ESTADO F #############
                    
        elif estado == 'F':            
            if char == 'a':
                estado = 'AG'                
            elif char == 'l':
                estado = 'AH'
            elif char == 'u':
                estado = 'AI'
            else:
                estado = 'C'
            
        ########### ESTADO G ##############
            
        elif estado == 'G':            
            if char == 'n':
                estado = 'AJ'
            else:
                estado = 'C'

        ############# ESTADO H ############
            
        elif estado == 'H':
            if char == 'e':
                estado = 'AK'
            else:
                estado = 'C'
            
        ############# ESTADO I ############
            
        elif estado == 'I':            
            if char == 'e':
                estado = 'AL'
            else:
                estado = 'C'

        ############ ESTADO J #############
            
        elif estado == 'J':
            if char == '>':
                if nro_token == token:
                    return ('relop', 'NE', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
            elif char == '=':
                if nro_token == token:
                    return ('relop', 'LE', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'         
            else:                 
                if nro_token == token:
                    return ('relop', 'LT', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            
        ############# ESTADO L ############
            

        elif estado == 'L':
            if nro_token == token:
                return ('Operador Aritimético', '-', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        
        ############# ESTADO M ############
            
        elif estado == 'M':            
            if nro_token == token:
                return ('Operador Aritimético', '+', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        
        ############ ESTADO N #############
            
        elif estado == 'N':
            if char !=  '*':
                if nro_token == token:
                    return ('Operador Aritimético', '/', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
                
            else:
                estado = 'AQ'                      
        
        ########### ESTADO O ##############
            
        elif estado == 'O':            
            if nro_token == token:
                return ('Operador Aritimético', '*', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
            

            
        ############ ESTADO Q #############
            
        elif estado == 'Q':
            if char != '=':
                if nro_token == token:
                 return ('Operador Aritmetico', '=', (linha, coluna)) 
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            else:                
                estado = 'AO'                
        
        ############ ESTADO R #############
            
        elif estado == 'R':            
            if char == '=':
                if nro_token == token:
                    return ('relop', 'GE', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
            else:                
                if nro_token == token:
                    return ('relop', 'GT', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
                    look_ahead = True
                    
            
        
        ############# ESTADO V ############
            
        elif estado == 'V':            
            if nro_token == token:
                return ('(', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
    
        
        ############# ESTADO Z ############
            
        elif estado == 'Z':

            if char == 'E':
                estado = 'AR'
            
            elif char == '.':
                estado = 'AS'
            elif char in NUMBER:
                estado = 'Z'
            else:
                if nro_token == token:
                    nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                    return ('NROINT', nro_elem, (linha, coluna))
                else:
                    nro_token +=1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True 

        #########################
        
        elif estado == 'AA':
            if char in LETRA_LOWER or char in LETRA_UPPER:
                estado = 'AT'

            else:
                estado = 'ERR'
            
        #########################

        elif estado == 'AB':
            if char == ' ' or char == '\n' or char == '\t':
                if char == '\n':
                    linha += 1
                    coluna = 0
                estado = 'A'

            else:
                strAux = ''
                estado = 'A'
                look_ahead = True 
                


        
        #########################

        elif estado == 'AD':
            if char == 'e':
                estado = 'AV'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AE':
            if char == 'a':
                estado = 'AW'

            else:
                estado = 'C'
                
        #########################

        elif estado == 'AF':
            if char == 'q':
                estado = 'AY'
            elif char == 't':
                estado = 'AX'
            else:
                estado = 'C'
                
        #########################
      
        elif estado == 'AG':
            if char == 'c':
                estado = 'AZ'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AH':
            if char == 'o':
                estado = 'BA'
            else:
                estado = 'C'
            
        #########################
        
        elif estado == 'AI':
            if char == 'n':
                estado = 'BB'
            else:
                estado = 'C'
                
        #########################
           
        elif estado == 'AJ':
            if char == 't':
                estado = 'BC'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AK':
            if char == 'p':
                estado = 'BD'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AL':
            if char == 'n':
                estado = 'BE'
            elif char not in ID:
                if nro_token == token:
                    return ('se', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True                               
                
            else:
                estado = 'C'
                
        ########### RELOPS ###########
    
        elif estado == 'AM':
            if nro_token == token:
                return ('relop', 'LE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
            
        elif estado == 'AN':            
            if nro_token == token:
                return  ('relop', 'NE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
            
            
        elif estado == 'AO': 
            if nro_token == token:
                return  ('relop', 'EQ', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 

            
        #########################
            
        elif estado == 'AQ':
            if char == '*':
                estado ='BF'
            else:
                estado = 'AQ'
                
        #########################
            
        elif estado == 'AR':
            if char == '+' or char == '-':
                estado = 'BG'

            elif char in NUMBER:
                estado = 'BH'

            else:
                estado = 'ERR'

        #########################
            
        elif estado == 'AS':
            if char in NUMBER:
                estado = 'BI'

            else:
                estado = 'ERR'
                
        #########################
        
        elif estado == 'AT':
            if char == "'":
                estado = 'BJ'

            else:
                estado = 'ERR'       
        
        #########################
        
        elif estado == 'AV':
            if char not in ID:                
                if nro_token == token:
                    return ('ate', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
                    look_ahead = True
            else:
                estado ='C'

        #########################
    
        elif estado == 'AW':
            if char == 'r':
                estado = 'BK'                
            else:
                estado = 'C'

        #########################
            
        elif estado == 'AX':
            if char == 'a':
                estado = 'BL'
            else:
                estado = 'C'

        #########################
            
        elif estado == 'AY':
            if char == 'u':
                estado = 'BM'
            else:
                estado = 'C'
        #########################
            
        elif estado == 'AZ':
            if char == 'a':
                estado = 'BN'
            else:
                estado = 'C'
    
        #########################
            
        elif estado == 'BA':
            if char == 'a':
                estado = 'BO'
            else:
                estado = 'C'

        #########################

        elif estado == 'BB':
            if char == 'c':
                estado = 'BP'
            else:
                estado = 'C'
        #########################

        elif estado == 'BC':
            if char not in ID:
                if nro_token == token:
                    return ('int', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BD':
            if char == 'i':
                estado = 'BQ'
            else:
                estado = 'C'
        #########################

        elif estado == 'BE':
            if char == 'a':
                estado = 'BR'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BF':
            if char == '/':
                strAux = ''
                estado = 'A'           
        
            else:
                estado = 'AQ'

        #########################

        elif estado == 'BG':
            if char in NUMBER:
                estado = 'BH'
            else:
                estado = 'ERR'
                
        #########################
        
        elif estado == 'BH':
            if char in NUMBER:
                estado = 'BH'
            else:
                if nro_token == token:
                    if nro_token == token:
                        nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                        return ('exp', nro_elem, (linha, coluna))
                else:
                    nro_token +=1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True

        #########################
        
        elif estado == 'BI':
            if char in NUMBER:
                estado = 'BI'
            elif char == '.':
                estado = 'ERR'
            elif char == 'E':
                estado = 'AR'
            else:
                if nro_token == token:
                    nro_elem = addTable(strAux, TABELA_SIMBOLO)
                    return ('frac', nro_elem, (linha, coluna))
                else:
                    nro_token +=1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True      

        #########################
        
        elif estado == 'BJ':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('letra', nro_elem, (linha, coluna))
            else:
                nro_token +=1
                strAux = ''
                estado = 'A'
        
        #########################
        
        elif estado == 'BK':
            if char not in ID:
                if nro_token == token:
                    return ('char', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True  
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BL':
            if char == 'o':
                estado = 'BT'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BM':
            if char == 'a':
                estado = 'BU'
            else:
                estado = 'C'

        #########################

        elif estado == 'BN':
            if char not in ID:
                if nro_token == token:
                    return ('faca', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True       
            else:
                estado = 'C'

        #########################f

        elif estado == 'BO':
            if char == 't':
                estado = 'BV'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BP':
            if char == 't':
                estado = 'BW'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BQ':
            if char == 't':
                estado = 'BX'
            else:
                estado = 'C'
        #########################

        elif estado == 'BR':
            if char == 'o':
                estado = 'BY'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BS':
            if char == 't':
                estado = 'CB'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BT':
            if char not in ID:
                if nro_token == token:
                    return ('entao', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            else:
                estado = 'C'
        #########################

        elif estado == 'BU':
            if char == 'n':
                estado = 'BS'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BV':
            if char not in ID:
                if nro_token == token:
                    return ('float', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            else:
                estado = 'C'
            
        #########################

        elif estado == 'BW':
            if char == 'i':
                estado = 'BZ'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BX':
            if char == 'a':
                estado = 'CA'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BY':
            if char not in ID:
                if nro_token == token:
                    return ('senao', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            else:
                estado = 'C'
            
        #########################

        elif estado == 'BZ':
            if char == 'o':
                estado = 'CC'
            else:
                estado = 'C'
        #########################

        elif estado == 'CA':
            if char in ID:
                estado = 'C'
            else:
                if nro_token == token:
                    return ('repita', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
                
        #########################

        elif estado == 'CB':
            if char == 'o':
                estado = 'CD'
            else:
                estado = 'C'

        #########################
            
        elif estado == 'CC':
            if char == 'n':
                estado = 'CE'
            else:
                estado = 'C'

            
        #########################

        elif estado == 'CD':
            
            if char in ID:
                estado = 'C'
            else:
                if nro_token == token:
                    return ('enquanto', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
                    
        #########################

        elif estado == 'CE':
            if char in ID:
                estado = 'C'
            else:
                if nro_token == token:
                    return ('function', NULL, (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
                    
        #########################
                

        else :
            return ('ERR', 'ERR', (linha,coluna))

    return('EOF', 'ERR', (linha, coluna))


        