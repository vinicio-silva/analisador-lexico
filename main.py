from analisadorlexico import *

def main():
    arquivo = open("codigo.txt", "r")
    cadeia = []
    i = 1

    # WHILE DO ANALISADOR
    while 1: 
        (token, atributo, (linha, coluna)) = getToken(arquivo, i)
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
        arquivo.seek(0,0)
        
    print(cadeia)        
    arquivo.close()

if __name__ == "__main__":
    main()