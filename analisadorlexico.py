from asyncio.windows_events import NULL
import string

TABELA_SIMBOLO = open("tabela-simbolo.txt", "r+")
LETRA_LOWER = list(string.ascii_lowercase)
LETRA_UPPER = list(string.ascii_uppercase)
NUMBER = [str(num) for num in range(9)]
CHAR_RESERVED = ['a', 'c', 'e', 'f', 'i', 'r', 's']
ID = LETRA_UPPER + LETRA_LOWER + NUMBER + '_'
SPECIAL_CHAR = ['<', '-', '+', '/', '*', '^', '>', '=', '.', ':', ',', ';', '(', ')', '{', '}', ' ', "'", '$']

def aceitacao():
    return "Aceito"


def addTable(char, table):   # Função para inserir na tabela de simbolos
    nelem = 1
    table.seek(0, 0)
    for linha in table:
        if (str(char+'\n')) == linha or str(char) == linha:
            return nelem
        nelem += 1

    table.writelines(char+"\n")
    return nelem


def getToken(file, token):
    estado = 'A'
    char = file.read(1)
    while 1: 
        #### Estado Inicial ####
        if estado == 'A':
            if char not in CHAR_RESERVED:
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

            elif char == '>':
                estado = 'Q'
            
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

            elif char == ' ':
                estado = 'AB'
            
            elif char == "'":
                estado = 'AA'
                
            else:
                estado = 'ERR'

                
        #########################
           
        elif estado == 'B':
            if char == 't':
                estado = 'AD'
            
            elif char in ID:
                estado = 'C'
            
            else:
                estado = 'AC'
        #########################
            
        elif estado == 'C':
            if char in ID:
                estado = 'C'
            else:
                estado = 'AC'
        #########################
            
        elif estado == 'D':
            if char == 'h':
                estado = 'AE'
            elif char in ID:
                estado = 'C'
            else:
                estado = 'AC'
            
        #########################
            
        elif estado == 'E':

            if char == 'n':
                estado = 'AF'

            elif char in ID: 
                estado = 'C'
            
            else:
                estado = 'AC'
        #########################
            
        
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
            
        #########################
            
        elif estado == 'G':
            
            if char == 'n':
                estado = 'AJ'

            elif char in ID:
                estado = 'C'

            else:
                estado = 'AC'

        #########################
            
        elif estado == 'H':
            if char == 'e':
                estado = 'AK'

            elif char in ID:
                estado = 'C'

            else:
                estado = 'AC' 
            
        #########################
            
        elif estado == 'I':
            
            if char == 'e':
                estado = 'AL'

            elif char in ID:
                estado = 'C'

            else:
                estado = 'AC' 
            
        #########################
            
        elif estado == 'J':

            if char == '>':
                estado = 'AN'
            elif char == '=':
                estado = 'AM'
            
            else: 
                return ('LT')
            
        #########################
            

        elif estado == 'L':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'M':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'N':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'O':
            return ('ESTADO FINAL')
            
        #########################
            
        elif estado == 'P':
            return ('ESTADO FINAL')
            
        #########################
            
        elif estado == 'Q':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'R':
            
            if char == '=':
                estado = 'AP'
            else:
                return ('GT')
            
        #########################
            
        elif estado == 'S':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'T':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'U':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'V':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'W':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'X':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'Y':
            return ('ESTADO FINAL')
        
        #########################
            
        elif estado == 'Z':

            if char == 'E':
                estado = 'AR'
            
            elif char == '.':
                estado = 'AS'
            elif char in NUMBER:
                estado = 'Z'
            else:
                return ('NRO INTEIRO', char)
            
            
        #########################
            pass
        
        elif estado == 'AA':
            if char in LETRA_LOWER or char in LETRA_UPPER:
                estado == 'AT'

            else:
                estado == 'ERR'
            
        #########################

        elif estado == 'AB':
            if char == ' ':
                estado == 'AB'

            else:
                estado == 'AU'
                
        #########################
            
        elif estado == 'AC':
            return aceitacao()
        
        #########################

        elif estado == 'AD':
            if char == 'e' or char == 'E':
                estado == 'AV'
                
            elif char in SPECIAL_CHAR:
                estado == 'AC'

            else:
                estado == 'C'
                
        #########################

        elif estado == 'AE':
            if char in SPECIAL_CHAR:
                estado == 'AC'

            elif char == 'a' or char == 'A':
                estado == 'AW'

            else:
                estado == 'C'
                
        #########################

        elif estado == 'AF':
            if char == 'Q' or char == 'q':
                estado == 'AY'

            elif char == 'T' or char == 't':
                estado == 'AX'

            elif char in SPECIAL_CHAR:
                estado == 'AC'

            else:
                estado == 'C'
                
        #########################
      
        elif estado == 'AG':
            if char == 'C' or char == 'c':
                estado == 'AZ'

            elif char in SPECIAL_CHAR :
                estado = 'AC'

            else:
                estado = 'C'
                
        #########################

        elif estado == 'AH':
            if char == 'o' or char == 'O':
                estado == 'BA'
                
            elif char in SPECIAL_CHAR :
                estado == 'AC'

            else:
                estado == 'C'
            
        #########################
        
        elif estado == 'AI':
            if char == 'n' or char == 'N':
                estado == 'BB'

            elif char in SPECIAL_CHAR:
                estado == 'AC'
                
            else:
                estado == 'C'
                
        #########################
           
        elif estado == 'AJ':
            if char == 't' or char == 'T':
                estado == 'BC'

            elif char in SPECIAL_CHAR:
                estado == 'AC'
                
            else:
                estado == 'C'
                
        #########################

        elif estado == 'AK':
            if char == 'P' or char == 'p':
                estado == 'BD'

            elif char in SPECIAL_CHAR :
                estado == 'AC'
                
            else:
                estado == 'C'
                
        #########################

        elif estado == 'AL':
            if char == 'N' or char == 'n':
                estado == 'BE'

            elif char in SPECIAL_CHAR:
                estado == 'SE'
                
            else:
                estado == 'C'
                
        #########################
    
        elif estado == 'AM':
            return 'Less-Equal'
        
        #########################
            
        elif estado == 'AN':
            return 'Not-Equal'
            
        #########################
            
        elif estado == 'AO':
            return 'Equal'
        
        #########################
        
        elif estado == 'AP':
            return 'Greater-Equal'
            
        #########################
            
        elif estado == 'AQ':
            if char == '*':
                estado == 'BF'

            else:
                estado == 'AQ'
                
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
        
        elif estado == 'AT':
            if char == "'":
                estado == 'BJ'

            else:
                estado == 'ERR'       
                
        #########################
            
        elif estado == 'AU':
            return 'White-Space'
        
        #########################
        
        elif estado == 'AV':
            if char == SPECIAL_CHAR or char == '_':
                estado == 'ATE'

            else:
                estado == 'C'

        #########################
    
        elif estado == 'AW':
            if char == 'r' or char == 'R':
                estado == 'BK'
                
            elif char in SPECIAL_CHAR:
                estado == 'AC'

            else:
                estado == 'C'

        #########################
            
        elif estado == 'AX':
            if char == 'a' or char == 'A':
                estado == 'BL'

            elif char in SPECIAL_CHAR:
                estado == 'AC'

            else:
                estado == 'C'

        #########################
            
        elif estado == 'AY':
            if char == 'u' or char == 'U':
                estado == 'BM'

            elif char in SPECIAL_CHAR:
                estado =='AC'
                
            else:
                estado == 'C'
        #########################
            
        elif estado == 'AZ':
            if char == 'a' or char == 'A':
                estado == 'BN'
            elif char in SPECIAL_CHAR:
                estado == 'AC'
            else:
                estado == 'C'
    
        #########################
            
        elif estado == 'BA':
            if char == 'a':
                estado = 'BO'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'

        #########################

        elif estado == 'BB':
            if char == 'c':
                estado = 'BO'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################

        elif estado == 'BC':
            if char in SPECIAL_CHAR:
                estado = 'INT'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BD':
            if char == 'i':
                estado = 'BQ'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################

        elif estado == 'BE':
            if char == 'a':
                estado = 'BR'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BF':
            if char == '/':
                estado = 'CMNT'
            else:
                estado = 'AQ'

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
            elif char in [' ', "'", '$']:
                estado = 'EXP'
            elif char == '.':
                estado = 'ERR'
            elif char == 'e':
                estado = 'AR'
            else:
                estado = 'FRAC'         

        #########################
        
        elif estado == 'BJ':
            return "Aceitação BJ"
        
        #########################
        
        elif estado == 'BK':
            if char in SPECIAL_CHAR:
                estado = 'CHAR'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BL':
            if char == 'o':
                estado = 'BT'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BM':
            if char == 'a':
                estado = 'BU'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'

        #########################

        elif estado == 'BN':
            if char in SPECIAL_CHAR:
                estado = 'FACA'
            else:
                estado = 'C'

        #########################

        elif estado == 'BO':
            if char == 't':
                estado = 'BV'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BP':
            if char == 't':
                estado = 'BW'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BQ':
            if char == 't':
                estado = 'BX'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################

        elif estado == 'BR':
            if char == 'o':
                estado = 'BY'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BS':
            if char == 't':
                estado = 'CB'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BT':
            if char in SPECIAL_CHAR:
                estado = 'ENTAO'
            else:
                estado = 'C'
        #########################

        elif estado == 'BU':
            if char == 'n':
                estado = 'BS'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################
        
        elif estado == 'BV':
            if char in SPECIAL_CHAR:
                estado = 'FLOAT'
            else:
                estado = 'C'
            
        #########################

        elif estado == 'BW':
            if char == 'i':
                estado = 'BZ'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
                
        #########################

        elif estado == 'BX':
            if char == 'a':
                estado = 'CA'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
                
        #########################
        
        elif estado == 'BY':
            if char in SPECIAL_CHAR:
                estado = 'SENAO'
            else:
                estado = 'C'
            
        #########################

        elif estado == 'BZ':
            if char == 'o':
                estado = 'CC'
            elif char in SPECIAL_CHAR:
                estado = 'AC'
            else:
                estado = 'C'
        #########################

        elif estado == 'CA':
            
            if char in ID:
                estado = 'C'
            else:
                estado = 'REPITA'
                
        #########################
            pass
        elif estado == 'CB':
            
            if char == 'o':
                estado = 'CD'

            elif char in ID:
                estado = 'C'
                
            else:
                estado = 'AC'

        #########################
            
        elif estado == 'CC':
            
            if char == 'n':
                estado = 'CE'
                
            elif char in ID:
                estado = 'C'
                
            else:
                estado = 'AC'

            
        #########################
            pass
        elif estado == 'CD':
            
            if char in ID:
                estado = 'C'

            else:
                estado = 'ENQUANTO'
        #########################
            pass
        elif estado == 'CE':

            if char in ID:
                estado = 'C'

            else:
                estado = 'FUNCTION'
        #########################
            pass
        else :
            print("Estado não reconhecido.")




        