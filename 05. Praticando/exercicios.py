# Única escolha sobre o conteúdo da aula
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres)
                  for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))

    print("{} => {:.2f}%".format(caractere, proporcao * 100))

# Para implementar no código as 10 letras mais frequentes nos textos cadastrados, utiliza-se a função "most_common(10)". Essa função faz a atribuição de uma variável e percorre-a registrando sua proporção e os caracteres. Então a função seria complementada com o seguinte código, aplicado antes do print:


mais_comuns = proporcoes.most_common(10)

for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))
