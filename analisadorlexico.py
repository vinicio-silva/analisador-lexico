from asyncio.windows_events import NULL
import string

TABELA_SIMBOLO = open("tabela-simbolo.txt", "r+")
LETRA_LOWER = list(string.ascii_lowercase)
LETRA_UPPER = list(string.ascii_uppercase)
NUMBER = [str(num) for num in range(9)]
CHAR_RESERVED = ['a', 'c', 'e', 'f', 'i', 'r', 's']
ID = LETRA_UPPER + LETRA_LOWER + NUMBER + ['_']
SPECIAL_CHAR = ['<', '-', '+', '/', '*', '^', '>', '=', '.', ':', ',', ';', '(', ')', '{', '}', ' ', "'"]

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
        
        ################### Estado Inicial #####################
        
        if estado == 'A':
            if char in ['b', 'd', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']:
                estado = 'C'
                
            elif char == 'a':
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
                estado = 'L'
            
            elif char == '+':
                estado = 'M'
            
            elif char == '/':
                estado = 'N'
            
            elif char == '*':
                estado = 'O'

            elif char == '^':
                estado = 'P'

            elif char == '=':
                estado = 'Q'

            elif char == '<':
                estado = 'J'

            elif char == '>':
                estado = 'R'
            
            elif char == '.':
                estado = 'ERR'
            
            elif char == ':':
                estado = 'S'

            elif char == ',':
                estado = 'U'
            
            elif char == ';':
                estado = 'T'

            elif char == '(':
                estado = 'V'
            
            elif char == ')':
                estado = 'W'

            elif char == '{':
                estado = 'X'
            
            elif char == '}':
                estado = 'Y'
            
            elif char in NUMBER:
                estado = 'Z'

            elif char == ' ' or char == '\n' or char == '\t':
                if char == '\n':
                    linha += 1
                estado = 'AB'
            
            elif char == "'":
                estado = 'AA'
                
            else:
                estado = 'ERR'

  ######################################################3              
            
        elif estado == 'C':
            if char in ID:
                estado = 'C'
            else:
                estado = 'AC'
   
            
        elif estado == 'J':
            if char == '>':
                estado = 'AN'
            elif char == '=':
                estado = 'AM'            
            else:                 
                if nro_token == token:
                    return ('relop', 'LT', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True



        ############## OPERADORES ARITMETICOS ###########
            
        ############ SUBTRACAO #############
            

        elif estado == 'L':
            if nro_token == token:
                return ('Operador Aritimético', '-', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        
        ############ SOMA #############
            
        elif estado == 'M':            
            if nro_token == token:
                return ('Operador Aritimético', '+', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        
        ########## DIVISAO ###############
            
        elif estado == 'N':

            if nro_token == token:
                return ('Operador Aritimético', '/', (linha, coluna))
            else:
                if char == '*':
                    estado = 'AQ'
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True                
        
        ############ MULTIPLICAÇÃO #############
            
        elif estado == 'O':            
            if nro_token == token:
                return ('Operador Aritimético', '*', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
            
        ############ EXPONENCIAL #############
            
        elif estado == 'P':           
            if nro_token == token:
                return ('Operador Aritimético', '^', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
            
        ############ ATRIBUICAO e ida  pro RELOP EQ #############
            
        elif estado == 'Q':
            if char != '=':
                estado = 'ATT'
            else:                
                estado = 'AO'
        
        elif estado == 'ATT':
            if nro_token == token:
                return ('Operador Aritmetico', '=', (linha, coluna)) 
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
                  
        
        #########################
            
        elif estado == 'R':            
            if char == '=':
                estado = 'GE'
            else:                
                if nro_token == token:
                    return ('relop', 'GT', (linha, coluna))
                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
                    look_ahead = True

        ############ DOIS PONTOS #############
            
        elif estado == 'S':
            if nro_token == token:
                return (':', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
        
        ############## PONTO E VIRGULA ###########
            
        elif estado == 'T':
            if nro_token == token:
                return (';', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
        
        ############ VIRGULA #############
            
        elif estado == 'U':
            if nro_token == token:
                return (',', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
        
        ############ ABRE PARENTESES #############
            
        elif estado == 'V':            
            if nro_token == token:
                return ('(', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        
        ############ FECHA PARENTESES #############
            
        elif estado == 'W':           
            if nro_token == token:
                return (')', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        
        ############ ABRE CHAVES #############
            
        elif estado == 'X':            
            if nro_token == token:
                return ('{', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
        
        ############ FECHA CHAVES #############
            
        elif estado == 'Y':            
            if nro_token == token:
                return ('}', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
        
        #########################
            
        elif estado == 'Z':

            if char == 'E':
                estado = 'AR'
            
            elif char == '.':
                estado = 'AS'
            elif char in NUMBER:
                estado = 'Z'
            else:
               estado = 'NINT'


        ############ CARACTERE ENTRE ASPAS SIMPLES #############
        
        elif estado == 'AA':
            if char in LETRA_LOWER or char in LETRA_UPPER:
                estado == 'AT'
            else:
                estado == 'ERR'

        elif estado == 'AT':
            if char == "'":
                estado == 'BJ'
            else:
                estado == 'ERR'

        elif estado == 'BJ':
             if nro_token == token:
                    nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                    return ('LETRA', nro_elem, (linha, coluna))
             else:
                    nro_token +=1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
        
        
        
            
        #########################

                
        ######## Estado aceitação de ID ###########    
        elif estado == 'AC':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('ID', nro_elem, (linha, coluna))
            else:
                nro_token +=1
                strAux = ''
                estado = 'A'
                look_ahead = True
        
        ###############  ATE ################

        elif estado == 'B':
            if char == 't':
                estado = 'AD'
            
            elif char in ID:
                estado = 'C'            
            else:
                estado = 'AC'

        elif estado == 'AD':
            if char == 'e':
                estado == 'AV'
                
            elif char not in ID:
                estado == 'AC'

            else:
                estado == 'C'


        elif estado == 'AV':
            if char not in ID:
                estado == 'ATE'
                look_ahead = True 

            else:
                estado == 'C'

        
        elif  estado == 'ATE':
            if nro_token == token:
                return ('se', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                
        ############## CHAR  #############

        elif estado == 'D':
            if char == 'h':
                estado = 'AE'
            elif char in ID:
                estado = 'C'
            else:
                estado = 'AC'

        elif estado == 'AE':
            if char not in ID:
                estado == 'AC'
            elif char == 'a':
                estado == 'AW'
            else:
                estado == 'C'  

        elif estado == 'AW':
            if char == 'r':
                estado == 'BK'
                
            elif char not in ID:
                estado == 'AC'

            else:
                estado == 'C' 

        elif estado == 'BK':
            if char not in ID:
                estado = 'CHAR'
                look_ahead = True 
            else:
                estado = 'C'
        
        elif estado == 'CHAR':
            if nro_token == token:
                return ('char', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 


        #### Estados de partida para enquanto e entao ####
        elif estado == 'E':
            if char == 'n':
                estado = 'AF'
            elif char in ID: 
                estado = 'C'            
            else:
                estado = 'AC'

        elif estado == 'AF':
            if char == 'q':
                estado == 'AY'

            elif char == 't':
                estado == 'AX'

            elif char not in ID:
                estado == 'AC'

            else:
                estado == 'C'

        ################ ENQUANTO ###################
        
        elif estado == 'AY':
            if char == 'u' or char == 'U':
                estado == 'BM'

            elif char not in ID:
                estado =='AC'
                
            else:
                estado == 'C'

        elif estado == 'BM':
            if char == 'a':
                estado = 'BU'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'BU':
            if char == 'n':
                estado = 'BS'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'BS':
            if char == 't':
                estado = 'CB'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        
        elif estado == 'CB':
            if char == 'o':
                estado = 'CD'
            elif char in ID:
                estado = 'C'      
            else:
                estado = 'AC'

        elif estado == 'CD':
            if char in ID:
                estado = 'C'
            else:
                estado = 'ENQUANTO'
                look_ahead = True 
        
        elif estado == 'ENQUANTO':
            if nro_token == token:
                return ('enquanto', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
            
    
      ################## ENTAO ##################
        elif estado == 'AX':
            if char == 'a' or char == 'A':
                estado == 'BL'

            elif char not in ID:
                estado == 'AC'

            else:
                estado == 'C'

        elif estado == 'BL':
            if char == 'o':
                estado = 'BT'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
        
        elif estado == 'BT':
            if char not in ID:
                estado = 'ENTAO'
                look_ahead = True 
            else:
                estado = 'C'

        elif estado == 'ENTAO':
            if nro_token == token:
                return ('entao', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
                
        
        ### Estado de partida para FACA, FLOAT, FUNCTION
        elif estado == 'F':            
            if char == 'a':
                estado = 'AG' 

            elif char == 'l':
                estado = 'AH'

            elif char == 'u':
                estado = 'AI'

            elif char in ID:
                estado = 'C'            
            else:
                estado = 'AC'

        ########### FACA ##############
        elif estado == 'AG':
            if char == 'c':
                estado == 'AZ'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'AZ':
            if char == 'a':
                estado == 'BN'
            elif char not in ID:
                estado == 'AC'
            else:
                estado == 'C'

        elif estado == 'BN':
            if char not in ID:
                estado = 'FACA'
                look_ahead = True 
            else:
                estado = 'C'

        elif estado == 'FACA':
            if nro_token == token:
                return ('faca', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                
        

        ########## FLOAT ############
        elif estado == 'AH':
            if char == 'o':
                estado == 'BA'    
            elif char not in ID:
                estado == 'AC'
            else:
                estado == 'C'
        
        elif estado == 'BA':
            if char == 'a':
                estado = 'BO'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'BO':
            if char == 't':
                estado = 'BV'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'BV':
            if char not in ID:
                estado = 'FLOAT'
                look_ahead = True
            else:
                estado = 'C'

        elif estado == 'FLOAT':
            if nro_token == token:
                return ('float', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'    
       
                
        ############ FUNCTION #############
        elif estado == 'AI':
            if char == 'n' or char == 'N':
                estado == 'BB'
            elif char not in ID:
                estado == 'AC'   
            else:
                estado == 'C'

        elif estado == 'BB':
            if char == 'c':
                estado = 'BO'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
        
        elif estado == 'BP':
            if char == 't':
                estado = 'BW'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'BW':
            if char == 'i':
                estado = 'BZ'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
        
        elif estado == 'BZ':
            if char == 'o':
                estado = 'CC'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'CC':
            if char == 'n':
                estado = 'CE'   
            elif char in ID:
                estado = 'C'   
            else:
                estado = 'AC'
        
        elif estado == 'CE':

            if char in ID:
                estado = 'C'
            else:
                estado = 'FUNCTION'
                look_ahead = True

        elif estado == 'FUNCTION':
            if nro_token == token:
                return ('function', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                

            
        ########### INT ##############
        elif estado == 'G':            
            if char == 'n':
                estado = 'AJ'
            elif char in ID:
                estado = 'C'
            else:
                estado = 'AC'

        elif estado == 'AJ':
            if char == 't':
                estado == 'BC'

            elif char not in ID:
                estado == 'AC'
                
            else:
                estado == 'C'

        elif estado == 'BC':
            if char not in ID:
                estado = 'INT'
                look_ahead = True
            else:
                estado = 'C'

        
        elif estado == 'INT':
            if nro_token == token:
                return ('int', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
                
        ############ REPITA #############

        elif estado == 'H':
            if char == 'e':
                estado = 'AK'
            elif char in ID:
                estado = 'C'
            else:
                estado = 'AC' 

        elif estado == 'AK':
            if char == 'P' or char == 'p':
                estado == 'BD'

            elif char not in ID :
                estado == 'AC'
                
            else:
                estado == 'C'
        
        elif estado == 'BD':
            if char == 'i':
                estado = 'BQ'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'

        elif estado == 'BQ':
            if char == 't':
                estado = 'BX'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
        
        elif estado == 'BX':
            if char == 'a':
                estado = 'CA'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
        
        elif estado == 'CA':
            
            if char in ID:
                estado = 'C'
            else:
                estado = 'REPITA'
                look_ahead = True
        
        elif estado == 'REPITA':
            if nro_token == token:
                return ('repita', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                
                
        

        ##### Estados de partida para SE e SENAO ##########
        elif estado == 'I':            
            if char == 'e':
                estado = 'AL'
            elif char in ID:
                estado = 'C'
            else:
                estado = 'AC' 

        elif estado == 'AL':
            if char == 'n':
                estado == 'BE'
            elif char not in ID:
                estado == 'SE'
                look_ahead = True     
            else:
                estado == 'C'
        
        ############# SE ############
        
        elif estado == 'SE':
            if nro_token == token:
                return ('se', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

                
        ############ SENAO #############

        elif estado == 'BE':
            if char == 'a':
                estado = 'BR'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
        
        elif estado == 'BR':
            if char == 'o':
                estado = 'BY'
            elif char not in ID:
                estado = 'AC'
            else:
                estado = 'C'
    
        elif estado == 'BY':
            if char not in ID:
                estado = 'SENAO'
                look_ahead = True 
            else:
                estado = 'C'
        
        elif estado == 'SENAO':
            if nro_token == token:
                return ('senao', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'       
        

        ############## RELOPS ###############
    
        elif estado == 'AM':
            if nro_token == token:
                return ('relop', 'LE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
            
        elif estado == 'AN':            
            if nro_token == token:
                return  ('relop', 'NE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'  
            
            
        elif estado == 'AO': 
            if nro_token == token:
                return  ('relop', 'EQ', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
        
        elif estado == 'GE':
            if nro_token == token:
                return ('relop', 'GE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
            
        ########### COMENTARIO #############
            
        elif estado == 'AQ':
            if char == '*':
                estado == 'BF'
            else:
                estado == 'AQ'
        
        elif estado == 'BF':
            if char == '/':
                estado = 'CMNT'
            else:
                estado = 'AQ'

        elif estado == 'CMNT':
            strAux = ''
            estado = 'A'  
        

         ########### SEPARADOR WS  #############
        elif estado == 'AB':
            if char == ' ' or char == '\n' or char == '\t':
                if char == '\n':
                    linha += 1
                estado == 'AB'

            else:
                estado == 'AU'
                look_ahead = True

        elif estado == 'AU':
            strAux = ''
            estado = 'A'

             
        #########################
            
        elif estado == 'AR':
            if char == '+' or char == '-':
                estado == 'BG'

            elif char in NUMBER:
                estado == 'BH'

            else:
                estado == 'ERR'

        #########################
            
        elif estado == 'AS':
            if char in NUMBER:
                estado == 'BI'

            else:
                estado = 'ERR'
                
        #########################
          
                
        #########################
            
       


        #########################

        elif estado == 'BG':
            if char in NUMBER:
                estado = 'BS'
            else:
                estado = 'ERR'
                
        #########################
        
        elif estado == 'BH':
            if char in NUMBER:
                estado = 'BH'
            else:
                estado = 'EXP'
                
        #########################
        
        elif estado == 'BI':
            if char in NUMBER:
                estado = 'BI'
            elif char in [' ', "'"]:
                estado = 'EXP'
            elif char == '.':
                estado = 'ERR'
            elif char == 'e':
                estado = 'AR'
            else:
                estado = 'FRAC'         

        #########################
        
        
        
        ############ ESTADO DE NUMERO INTEIRO ###########
        
        
        elif estado == 'NINT':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('NROINT', nro_elem, (linha, coluna))
            else:
                nro_token +=1
                strAux = ''
                estado = 'A'
                look_ahead = True
        
        ############ ESTADO DE EXPONENCIAL #############
        
        elif estado == 'EXP':
           if nro_token == token:
                nro_elem= addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('EXP', nro_elem, (linha, coluna))
           else:
                nro_token +=1
                strAux = ''
                estado = 'A'
                look_ahead = True
        
        ########## ESTADO FRAÇÃO #############
        
        elif estado == 'FRAC':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('FRAC', nro_elem, (linha, coluna))
            else:
                nro_token +=1
                strAux = ''
                estado = 'A'
                look_ahead = True
          
        #########################
        
        else :
            return ('ERR', 'ERR', (linha,coluna))

    return('EOF', 'ERR', (linha, coluna))


        