# Python Collections parte 2: conjuntos e dicionários

Aprendendo a trabalhar com conjuntos, variações de dicionários e diversas coleções ao mesmo tempo.

1. [Conjuntos](#1-conjuntos)
2. [Operações](#2-operações)
3. [Dicionários](#3-dicionários)
4. [Variações de dicionários](#4-variações-de-dicionários)
5. [Praticando](#5-praticando)

Saiba mais sobre o curso [aqui](https://cursos.alura.com.br/course/python-collections-conjuntos-e-dicionarios) ou acompanhe minhas anotações abaixo. ⬇️

## 1. Conjuntos

### **Trabalhando com conjuntos, os sets**

Conjuntos podem ser feitos através de listas, porém as listas aceitam repetição de elementos. Então, ao unir duas listas, todos os valores erão agrupados, inclusive os já existentes.

```py
# criando um conjunto a partir de listas
id_alunos_frontend = [12, 31, 47, 23]
id_alunos_backend = [17, 31, 23, 59]

# ao criar uma lista contendo uma cópia dos alunos front e acrescentando os alunos de back...
id_alunos_fullstack = id_alunos_frontend.copy()
id_alunos_fullstack.extend(id_alunos_backend)
id_alunos_fullstack

# ...o resultado é a união das listas, porém ocorre repetição dos alunos que estão em ambas as turmas
[12, 31, 47, 23, 17, 31, 23, 59]
```

- `.copy()` método que cria a cópia de uma lista já existente e retorna uma nova lista
- `.extend()` método que adiciona todos os elementos de um iterável ao final da lista

Se a ideia é filtrar itens iguais, pode-se utilizar o `set` que é uma coleção de dados únicos. Set utiliza chaves `{}` para referenciar conjuntos. Por padrão, um conjunto não possui ordem nos elementos.

```py
# utilizando chaves, cria-se um conjunto não ordenado com os itens da lista uma única vez
id_alunos_frontend = {12, 31, 47, 23}
id_alunos_backend = {17, 31, 23, 59}

# o set une esses conjuntos e faz a interseção dos elementos iguais
for aluno in set(id_alunos_fullstack):
    print(aluno)

# o resultado ainda é a união das listas, mas é feita uma interseção dos elementos, sem repetição
12, 31, 47, 23, 17, 59

# é possível ainda fazer uma comparação com o operador "ou"
usuarios_data_science | usuarios_machine_learning

# isso retorna a união dos conjuntos de elementos
{12, 17, 23, 31, 47, 59}
```

### **Mais operações de conjuntos**

> Usos comuns para conjuntos incluem a verificação eficiente da existência de objetos e a eliminação de itens duplicados. Conjuntos também suportam operações matemáticas como **união, interseção, diferença e diferença simétrica**.

- Para criar um conjunto vazio precisa, necessariamente, usar a função `set()`.
- Para criar um dicionário vazio ou uma estrutura de dados pode usar chaves `{}`.

```py
# realizando operações com conjuntos
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_data_science | usuarios_machine_learning   # "| = ou" equivale a união dos conjuntos
{13, 15, 23, 42, 43, 56}

usuarios_data_science & usuarios_machine_learning   # "& = e" equivale a interseção dos conjuntos
{23, 56}

usuarios_data_science - usuarios_machine_learning   # "-" remove números que se repetem no outro conjunto
{15, 43}

usuarios_data_science ^ usuarios_machine_learning   # "^" equivale ao "ou" só que remove os repetidos
{13, 15, 42, 43}
```

## 2. Operações

### **Outro tipo de conjunto e conjuntos de outros tipos**

É possível modificar o conjunto em tempo real. Porém, ao invés de utilizar `.append()`, já que conjuntos não possuem índice e o append adiciona ao final da lista. No `set` utiliza-se o `.add()` para adicionar um elemento ao conjunto, sem se preocupar com a ordem dos elementos.

- Lembrando que ao adicionar um elemento que já existe, a lista não será alterada.

Assim como as listas e diferente das tuplas, os conjuntos são mutáveis. Podendo **adicionar, remover, alterar e limpar** um conjunto existente. Contudo, existe um tipo de conjunto que é imutável, o `frozenset()`, seu conteúdo não pode ser alterado depois da criação, podendo ser utilizado como chave de dicionário ou elemento de outro conjunto para comparações e operações.

> Então o frozenset() também faz parte do nosso dia a dia, quando queremos trabalhar com elementos e conjuntos, podemos acabar optando agora por listas, por tuplas, às vezes arrays ou arrays do numPy, que é mais comum, às vezes vamos utilizar um conjunto, às vezes um conjunto congelado imutável.

```py
usuarios = {1, 5, 76, 34, 52, 13, 17}

usuarios.add(13)    # o 13 já está no conjunto
usuarios.add(75)

usuarios = frozenset(usuarios)  # conjunto fechado

usuarios.add(36)    # o frozenset não deixa adicionar elementos
```

Conjuntos podem ser utilizados com strings e com objetos também, não só com números inteiros. Utilizando a função `.split()` pode-se quebrar todo o texto em partes, gerando uma lista de palavras. É possível, inclusive, transformar esse texto em um conjunto. Nesse caso, palavras repetidas será removidas.

```py
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

meu_texto.split()       # quebra o texto da lista em pedaços
set(meu_texto.split())  # quebra o texto e transforma em conjunto, então não repete palavras
```

## 3. Dicionários

### **Trabalhando com dicionários**

Dicionários são estruturas de dados usadas para armazenar dados em pares. Relacionados por `chave : valor`. É uma coleção ordenada, mutável e não permite duplicidade dos dados.

```py
# criando o dicionário
car = {
  "brand": "Porsche",
  "model": "Carrera 911",
  "year": 1964
}

# identificando o conjunto como "dict"
type(car)

# identificando o valor "Porsche" através da chave
car["brand"]

# adiciona um elemento ao dicionário
car["color"] = blue
```

### **Mais operações com dicionários**

> Diferente de sequências que são indexadas por inteiros, dicionários são indexados por chaves (keys), que podem ser de qualquer tipo imutável (como strings e inteiros).

- `dict` cria um dicionário
- `get` verifica os elementos
- `del` remove um elemento
- `in` busca as chaves, não os valores
- `keys` retorna as chaves
- `values` retorna os valores
- `items` percorre linha a linha

```py
# criando um dicionário pelo método "dict()"
car = dict(brand = "Porsche", model = "Carrera 911", year = 1964)

# buscando o valor "Carrera 911" pela sua chave e retorna 0 se não achar
car.get("model", 0)

# removendo um valor do dicionário
del car["color"]

# retorna "True" se existir a chave específicada
"year" in car

# retorna "False" porque não busca valores
1964 in car

# retorna um valor como "True"
1964 in car.values()
```

## 4. Variações de dicionários

### **Default dict**

> O `defaultdict` é uma subclasse da classe de dicionário que retorna um objeto semelhante a um dicionário. Diferente do dicionário comum, o defaultdict nunca gera um "KeyError". Ele fornece um valor padrão para a chave que não existe.

```py
# importa o dicionário
from collections import defaultdict

# função que define um valor inexistente
def def_value():
  return "Not Present"

# criando o dicionário
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"]) # retorna 1
print(d["b"]) # retorna 2
print(d["c"]) # retorna "Not present"
```

Algumas funções utilizadas em dicionários, formatam `strings` para um controle melhor do código:

- `lower()` devolve todos os caracteres em minúsculo
- `upper()` devolve todos os caracteres em maiúsculo
- `split()` quebra todo o texto em palavras
- `replace()` devolve uma cópia modificada do texto
- `join` função de concatenação de strings
- `reverse` função que inverte a direção da string

```py
# lower to upper
string="python at guru99"
print(string.upper())

# upper to lower
string="PYTHON AT GURU99"
print(string.lower())

# split
word="guru99 career guru99"		
print(word.split(' '))

# replace
oldstring = 'I like Guru99' 
newstring = oldstring.replace('like', 'love')
print(newstring)

# join
print(":".join("Python"))

# reverse
string="12345"		
print(''.join(reversed(string)))
```

Strings são imutáveis, então para verificar os itens que foram modificados pelo `replace`, deve-se criar uma nova lista a partir da original e imprimir a nova lista. No exemplo acima, a "oldstring" ainda contém o "like".

### **Counter**

O `defaultdict()` funciona também como um contador, mas existe uma função específica para isso, o `Counter()`.
O counter é uma subclasse do dicionário que serve para contar objetos. Sendo que os elementos desse objeto são armazenados como chaves e suas contagens armazenadas como valores.

```py
# texto de exemplo, formatado em minúsculo
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

# utilizando o defaultdict para não retornar erro
# utilizando o int para retornar zero como valor padrão
aparicoes = defaultdict(int)

# fazendo um loop para contar as palavras do texto
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
aparicoes

# utilizando o contador com o split tem-se o mesmo resultado
aparicoes = Counter(meu_texto.split())
aparicoes
```

## 5. Praticando

### **Colocando tudo em prática**

Reforçando o aprendizado do módulo de dicionários e das coleções em Python. Adicionando, também, novas funções e operações possíveis de serem realizadas nos exercícios propostos.

- `sum` soma os caracteres do texto

```py
# a partir de um texto qualquer em que se queira contar letras em minúsculo
aparicoes = Counter(texto1.lower())

# é possível somar os valores da quantidade de caracteres que aparecem no texto
total_de_caracteres = sum(aparicoes.values())

# e calcular a frequência com que esses caracteres aparecem e suas proporções
proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]

# criando um dicionário a partir disso e retornando nele os caracteres que mais aparecem
proporcoes = Counter(dict(proporcoes))
proporcoes.most_common(10)

# por fim, cria uma função que engloba todas as modificações, operações e formatações realizados
def analisa_frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

# para devolver as 10 letras que mais aparecem no texto e sua porcentagem de aparição
analisa_frequencia_letras(texto1)
```

> Usando most_common passamos por parâmetro o número de elementos que queremos, no nosso caso foi 10. Ele vai nos retornar uma lista de tuplas com os elementos e suas devidas proporções.

⬆️ [Voltar ao topo](#python-collections-parte-2-conjuntos-e-dicionários) ⬆️