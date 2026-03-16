frase = 'a rata roeu a roupa do rei de roma'
ocorrencias = {}
palavras = frase.split()

for palavra in palavras:
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1

print(ocorrencias)