# texto utilizado como exemplo na aula
aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

# retorna todas as chaves
for elemento in aparicoes:
    print(elemento)


# mostra as chaves
for elemento in aparicoes.keys():
    print(elemento)


# mostra os valores
for elemento in aparicoes.values():
    print(elemento)


# mostra chave e valor
for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])


for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)


# mostra chave e valor em tuplas
for elemento in aparicoes.items():
    print(elemento)


# mostra chave e valor desempacotando as tuplas
for chave, valor in aparicoes.items():
    print(chave, "=", valor)
