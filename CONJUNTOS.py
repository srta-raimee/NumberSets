#LARISSA RAIMEE GOMES

def cartesiano(conj1, conj2):
    retorno = []
    for x in conj1:
        for y in conj2:
            novo_elemento = [x, y]
            retorno.append(novo_elemento)

    return retorno

nome_arquivo = str(input("insira o nome do arquivo:"))

partes = nome_arquivo.split(".")

nome_arquivo = partes[0] + ".txt"

with open(nome_arquivo, "r") as arquivo:

    linhas = arquivo.readlines()

    cont1 = 0
    for x in linhas:
        item = x.split("\n")
        linhas[cont1] = item[0]

        cont1+=1

cont = 1
repeticoes = int(linhas[0])
while repeticoes:
    conjunto1 = set(linhas[cont + 1].split(", "))
    conjunto2 = set(linhas[cont + 2].split(", "))

    if linhas[cont] == "U" or linhas[cont] == "u":
        retorno = conjunto1 | conjunto2
        print("União: Conjunto 1" + str(conjunto1) + ",Conjunto 2" + str(conjunto2) + ",Resultado: " + str(retorno))

    elif linhas[cont] == "I" or linhas[cont] == "i":
        retorno = conjunto1 & conjunto2
        print("Interseção: Conjunto 1" + str(conjunto1) + ",Conjunto 2" + str(conjunto2) + ",Resultado: " + str(retorno))

    elif linhas[cont] == "D" or linhas[cont] == "d":
        retorno = conjunto1 - conjunto2
        print("Diferença: Conjunto 1" + str(conjunto1) + ",Conjunto 2" + str(conjunto2) + ",Resultado: " + str(retorno))

    elif linhas[cont] == "C" or linhas[cont] == "c":
        retorno = cartesiano(conjunto1, conjunto2)
        print("Produto Cartesiano: Conjunto 1" + str(conjunto1) + ",Conjunto 2" + str(conjunto2) + ",Resultado: " + str(retorno))

    cont += 3
    repeticoes -= 1