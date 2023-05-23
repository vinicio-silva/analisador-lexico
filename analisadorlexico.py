from asyncio.windows_events import NULL
import string

TABELA_SIMBOLO = open("tabela-simbolo.txt", "r+")
LETRA_LOWER = list(string.ascii_lowercase)
LETRA_UPPER = list(string.ascii_uppercase)
NUMBER = [str(num) for num in range(9)]
CHAR_RESERVED = ['a', 'c', 'e', 'f', 'i', 'r', 's']
ID = LETRA_UPPER + LETRA_LOWER + NUMBER + ['_']

token = []
token.append(('nome', 'atributo'))



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
        #### Estado Inicial ####
        
        if estado == 'A':
            if look_ahead is False:
                char = file.read(1) 
                coluna +=1
            strAux = strAux + str(char)
            look_ahead = False

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
                estado = 'AB'
            
            elif char == "'":
                estado = 'AA'

            elif char in ID:
                estado = 'C'                
                
            else:
                estado = 'ERR'           
        
        elif estado == 'ERR':
            if not char:
                break
            else:
                return('ERR', 'ERR', (linha,coluna))
            
        ############ ESTADO B #############
           
        elif estado == 'B':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 't':
                estado = 'AD'         
            else:
                estado = 'C'
                
        ############ ESTADO C #############
            
        elif estado == 'C':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in ID:
                estado = 'C'
            else:
                estado = 'AC'

        ########### ESTADO D ##############
            
        elif estado == 'D':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'h':
                estado = 'AE'
            else:
                estado = 'C'
                            
        ############ ESTADO E #############
            
        elif estado == 'E':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'n':
                estado = 'AF'          
            else:
                estado = 'C'
                look_ahead = True
                
        ############ ESTADO F #############
                    
        elif estado == 'F':   
            char = file.read(1)
            strAux = strAux + str(char)         
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
            char = file.read(1)
            strAux = strAux + str(char)         
            if char == 'n':
                estado = 'AJ'
            else:
                estado = 'C'

        ############# ESTADO H ############
            
        elif estado == 'H':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'e':
                estado = 'AK'
            else:
                estado = 'C'
            
        ############# ESTADO I ############
            
        elif estado == 'I':
            char = file.read(1)
            strAux = strAux + str(char)           
            if char == 'e':
                estado = 'AL'
            else:
                estado = 'C'

        ############ ESTADO J #############
            
        elif estado == 'J':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == '>':
                if nro_token == token:
                    estado = 'AN'

                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
            elif char == '=':
                if nro_token == token:
                    estado = 'AM'

                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'         
            else:                 
                if nro_token == token:
                    estado = 'LT'

                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
        
        ############ ESTADO N #############
            
        elif estado == 'N':
            char = file.read(1)
            strAux = strAux + str(char)
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

        ############ ESTADO Q #############
            
        elif estado == 'Q':
            char = file.read(1)
            strAux = strAux + str(char)
            if char != '=':
                if nro_token == token:
                    estado = 'ATT'

                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True
            else:                
                estado = 'AO'                
        
        ############ ESTADO R #############
            
        elif estado == 'R':
            char = file.read(1)
            strAux = strAux + str(char)            
            if char == '=':
                if nro_token == token:
                    estado = 'GE'

                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
            else:                
                if nro_token == token:
                    estado = 'GT'

                else:
                    nro_token += 1
                    strAux = ''
                    estado = 'A' 
                    look_ahead = True
        
        ############# ESTADO Z ############
            
        elif estado == 'Z':
            char = file.read(1)
            strAux = strAux + str(char)

            if char == 'E':
                estado = 'AR'
            
            elif char == '.':
                estado = 'AS'
            elif char in NUMBER:
                estado = 'Z'
            else:
                if nro_token == token:
                    estado = 'NINT'

                else:
                    nro_token +=1
                    strAux = ''
                    estado = 'A'
                    look_ahead = True 

        #########################
        
        elif estado == 'AA':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in LETRA_LOWER or char in LETRA_UPPER:
                estado = 'AT'

            else:
                estado = 'ERR'
            
        #########################

        elif estado == 'AB':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == ' ' or char == '\n' or char == '\t':
                if char == '\n':
                    linha += 1
                    coluna = 0
                estado = 'AB'

            else:
                estado = 'AU'
                        
        #########################

        elif estado == 'AD':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'e':
                estado = 'AV'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AE':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'AW'

            else:
                estado = 'C'
                
        #########################

        elif estado == 'AF':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'q':
                estado = 'AY'
            elif char == 't':
                estado = 'AX'
            else:
                estado = 'C'
                
        #########################
      
        elif estado == 'AG':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'c':
                estado = 'AZ'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AH':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'o':
                estado = 'BA'
            else:
                estado = 'C'
            
        #########################
        
        elif estado == 'AI':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'n':
                estado = 'BB'
            else:
                estado = 'C'
                
        #########################
           
        elif estado == 'AJ':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 't':
                estado = 'BC'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AK':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'p':
                estado = 'BD'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'AL':
            char = file.read(1)
            strAux = strAux + str(char)

            if char == 'n':
                estado = 'BE'
            elif char not in ID:
                    estado = 'SE'
            else:
                estado = 'C'
                
        ########### RELOPS <- ARRUMAR  ###########
    
        elif estado == 'AM':
            char = file.read(1)
            strAux = strAux + str(char)
            if nro_token == token:
                return ('relop', 'LE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
            
        elif estado == 'AN':  
            char = file.read(1)
            strAux = strAux + str(char)          
            if nro_token == token:
                return  ('relop', 'NE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
            
            
        elif estado == 'AO': 
            char = file.read(1)
            strAux = strAux + str(char)
            if nro_token == token:
                return  ('relop', 'EQ', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A' 
            
        #########################
            
        elif estado == 'AQ':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == '*':
                estado ='BF'
            else:
                estado = 'AQ'
                
        #########################
            
        elif estado == 'AR':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == '+' or char == '-':
                estado = 'BG'

            elif char in NUMBER:
                estado = 'BH'

            else:
                estado = 'ERR'

        #########################
            
        elif estado == 'AS':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in NUMBER:
                estado = 'BI'

            else:
                estado = 'ERR'
                
        #########################
        
        elif estado == 'AT':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == "'":
                estado = 'BJ'

            else:
                estado = 'ERR'       
        
        #########################
        
        elif estado == 'AV':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:                
                estado = 'ATE'
            else:
                estado ='C'

        #########################
    
        elif estado == 'AW':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'r':
                estado = 'BK'                
            else:
                estado = 'C'

        #########################
            
        elif estado == 'AX':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'BL'
            else:
                estado = 'C'

        #########################
            
        elif estado == 'AY':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'u':
                estado = 'BM'
            else:
                estado = 'C'
        #########################
            
        elif estado == 'AZ':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'BN'
            else:
                estado = 'C'
    
        #########################
            
        elif estado == 'BA':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'BO'
            else:
                estado = 'C'

        #########################

        elif estado == 'BB':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'c':
                estado = 'BP'
            else:
                estado = 'C'
        #########################

        elif estado == 'BC':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:
                estado = 'INT'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BD':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'i':
                estado = 'BQ'
            else:
                estado = 'C'
        #########################

        elif estado == 'BE':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'BR'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BF':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == '/':
                estado = 'CMNT'                 
            else:
                estado = 'AQ'

        #########################

        elif estado == 'BG':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in NUMBER:
                estado = 'BH'
            else:
                estado = 'ERR'
                
        #########################
        
        elif estado == 'BH':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in NUMBER:
                estado = 'BH'
            else:
                estado = 'EXP'

        #########################
        
        elif estado == 'BI':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in NUMBER:
                estado = 'BI'
            elif char == '.':
                estado = 'ERR'
            elif char == 'E':
                estado = 'AR'
            else:
                estado = 'FRAC'   

        #########################
        
        elif estado == 'BJ':
            char = file.read(1)
            strAux = strAux + str(char)
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('letra', nro_elem, (linha, coluna))
            else:
                nro_token +=1
                strAux = ''
                estado = 'A'
        
        #########################
        
        elif estado == 'BK':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:
                estado = 'CHAR' 
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BL':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'o':
                estado = 'BT'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BM':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'BU'
            else:
                estado = 'C'

        #########################

        elif estado == 'BN':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:
                estado = 'FACA'    
            else:
                estado = 'C'

        #########################f

        elif estado == 'BO':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 't':
                estado = 'BV'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BP':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 't':
                estado = 'BW'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BQ':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 't':
                estado = 'BX'
            else:
                estado = 'C'
        #########################

        elif estado == 'BR':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'o':
                estado = 'BY'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BS':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 't':
                estado = 'CB'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BT':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:
                estado = 'ENTAO'
            else:
                estado = 'C'
        #########################

        elif estado == 'BU':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'n':
                estado = 'BS'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BV':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:
                estado = 'FLOAT'
            else:
                estado = 'C'
            
        #########################

        elif estado == 'BW':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'i':
                estado = 'BZ'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BX':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'a':
                estado = 'CA'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BY':
            char = file.read(1)
            strAux = strAux + str(char)
            if char not in ID:
                estado = 'SENAO'
            else:
                estado = 'C'
            
        #########################

        elif estado == 'BZ':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'o':
                estado = 'CC'
            else:
                estado = 'C'
        #########################

        elif estado == 'CA':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in ID:
                estado = 'C'
            else:
                estado = 'REPITA'
                
        #########################

        elif estado == 'CB':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'o':
                estado = 'CD'
            else:
                estado = 'C'

        #########################
            
        elif estado == 'CC':
            char = file.read(1)
            strAux = strAux + str(char)
            if char == 'n':
                estado = 'CE'
            else:
                estado = 'C'

            
        #########################

        elif estado == 'CD':
            char = file.read(1)
            strAux = strAux + str(char)
            
            if char in ID:
                estado = 'C'
            else:
                estado = 'ENQUANTO'
        #########################

        elif estado == 'CE':
            char = file.read(1)
            strAux = strAux + str(char)
            if char in ID:
                estado = 'C'
            else:
                estado = 'FUNCTION'
                    

            # Estados finais (?)

        ######## Estado final do ID ########

        elif estado == 'AC':
            if nro_token == token:
                print('a strAux eh: ' + strAux)
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('ID', nro_elem, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        ######## Estado final numeros ########
        
        # Nro Inteiro

        elif estado == 'NINT':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('NROINT', nro_elem, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
            

        # nro Frac

        elif estado == 'FRAC':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('frac', nro_elem, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True


        # nro Exp

        elif estado == 'EXP':
            if nro_token == token:
                nro_elem = addTable(strAux[:-1], TABELA_SIMBOLO)
                return ('exp', nro_elem, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        ######## Estado final palavras reservadas #######

        # CHAR

        elif estado == 'CHAR':
            if nro_token == token:
                return ('char', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # FLOAT

        elif estado == 'FLOAT':
            if nro_token == token:
                return ('float', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # INT

        elif estado == 'INT':
            if nro_token == token:
                return ('int', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # FUNCTION

        elif estado == 'FUNCTION':
            if nro_token == token:
                return ('function', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
    
        # SE
        
        elif estado == 'SE':
            if nro_token == token:
                return ('se', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
        
        # ENTAO

        elif estado == 'ENTAO':
            if nro_token == token:
                return ('entao', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True


        # SENAO

        elif estado == 'SENAO':
            if nro_token == token:
                return ('senao', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # ENQUANTO

        elif estado == 'ENQUANTO':
            if nro_token == token:
                return ('enquanto', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # FACA

        elif estado == 'FACA':
            if nro_token == token:
                return ('faca', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # REPITA

        elif estado == 'REPITA':
            if nro_token == token:
                return ('repita', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # ATE

        elif estado == 'ATE':
            if nro_token == token:
                return ('ate', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        ####### SEPARADOR WS #######

        elif estado == 'AU':
                strAux = ''
                estado = 'A'
                look_ahead = True 

        ####### COMENTARIO #######

        elif estado == 'CMNT':
            strAux = ''
            estado = 'A'
            look_ahead = True

        ####### RELOP #######

        # LT
        elif estado == 'LT':
            if nro_token == token:
                 return ('RELOP', 'LT', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True
           

        # NE
        elif estado == 'AN':
            if nro_token == token:
                return ('RELOP', 'NE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
        # LE

        elif estado == 'AM':
            if nro_token == token:
                return ('RELOP', 'LE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # GT

        elif estado == 'GT':
            if nro_token == token:
                return ('RELOP', 'GT', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # GE

        elif estado == 'GE':
            if nro_token == token:
                return ('RELOP', 'GE', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # EQ

        elif estado == 'AO':
            if nro_token == token:
                return ('RELOP', 'EQ', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        ####### OPERADORES ARITMETICOS #######

        # SUBTRACAO

        elif estado == 'L':
            if nro_token == token:
                return ('Operador Aritimético', '-', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
            

        # SOMA

        elif estado == 'M':
            if nro_token == token:
                return ('Operador Aritimético', '+', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # DIVISAO
        
        elif estado == 'DIV':
            if nro_token == token:
                return ('Operador Aritimético', '/', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True

        # MULTIPLICACAO

        elif estado == 'O':
            if nro_token == token:
                return ('Operador Aritimético', '*', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'


        # EXPONENCIAL

        elif estado == 'P':
            if nro_token == token:
                return ('Operador Aritimético', '^', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        

        # ATRIBUICAO

        elif estado == 'ATT':
            if nro_token == token:
                return ('Operador Aritimético', '=', (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                look_ahead = True



        ####### SIMBOLOS NORMAIS ##########

        # DOIS PONTOS

        elif estado == 'S':
            if nro_token == token:
                return (':', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
            

        # VIRGULA
        elif estado == 'U':
            if nro_token == token:
                return (',', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # PONTO E VIRGULA

        elif estado == 'T':
            if nro_token == token:
                return (';', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # PARENTESES

        # ABRE PARENTESES
        elif estado == 'V':
            if nro_token == token:
                return ('(', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # FECHA PARENTESES

        elif estado == 'W':
            if nro_token == token:
                return (')', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'


        # CHAVES

        # ABRE CHAVES
        elif estado == 'X':
            if nro_token == token:
                return ('{', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'

        # FECHA CHAVES

        elif estado == 'Y':
            if nro_token == token:
                return ('}', NULL, (linha, coluna))
            else:
                nro_token += 1
                strAux = ''
                estado = 'A'
                        
        #########################

    return('EOF', 'EOF', (linha, coluna))