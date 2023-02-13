# Contando valores
texto = "Bem vindo meu nome é Elias irei falar sobre os meus gostos eu gosto muito de cachorros e gatos eu gosto também de beber café"
texto = texto.lower()

# A forma mais simples de contar as palavras do texto acima é utilizando o Counter

aparicoes = Counter(texto.split())

# Ele quebra o texto em partes e mostra a quantidade de vezes que a palavra apareceu no texto


# lower to upper
string = "python at guru99"
print(string.upper())               # retorna "PYTHON AT GURU99"

# upper to lower
string = "PYTHON AT GURU99"
print(string.lower())               # retorna "python at guru99"

# split
word = "guru99 career guru99"
print(word.split(' '))              # retorna "['guru99', 'career', 'guru99']"

# replace
oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
print(newstring)                    # retorna "I love Guru99"

# join
print(":".join("Python"))           # retorna "P:y:t:h:o:n"

# reverse
string = "12345"
print(''.join(reversed(string)))    # retorna "54321"
