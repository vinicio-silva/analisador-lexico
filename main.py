from analisadorlexico import *

def main():
    file = open("codigo.txt", "r")
    
    cadeia = []
    i = 1

    while 1: 
        (token, atributo, (linha, coluna)) = getToken(file, i)
        
        if token == 'EOF':
            print('Fim do arquivo')
            break
        if token == 'ERR':
            print('Erro na linha: ' + str(linha) + ' e coluna: ' + str(coluna))
            break
        if atributo == NULL:
            atributo = 'Atributo nulo'        

        print("Nome: " + str(token) + ', ' + 'Atributo: ' + str(atributo))
        
        cadeia = cadeia + [(token, atributo)]
        
        i += 1
        
        file.seek(0,0)
        
    print(cadeia)    
        
    file.close()

if __name__ == "__main__":
    main()