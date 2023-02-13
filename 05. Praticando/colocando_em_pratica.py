# Testando o uso de diversas coleções

# importa o Counter
from collections import Counter


texto1 = """A Engenharia de Dados é a área responsável por desenvolver, implementar e manter esse ambiente, que chamamos de Pipeline. É nele que vamos criar todas as etapas relacionadas ao fluxo de dados, desde a extração, passando pelo armazenamento, até a distribuição dos dados para consumo.

Um bom exemplo do impacto da Engenharia de Dados é nos ramos de administração e marketing de uma empresa. Principalmente em empresas que contém uma pluralidade de perfil de clientes, entender como o comportamento do consumidor pode trazer grandes benefícios para o futuro da empresa é um passo importante.

Por isso, empresas de streaming de mídia como a Netflix, por exemplo, investem constantemente em engenheiros para construir pipelines eficientes e disponibilizar dados com maior qualidade para as demais áreas de dados.

São as pessoas engenheiras de dados que cuidam dos enormes armazenamentos dos dados e fornecem o acesso a eles, para que a pessoa Cientista de Dados, que utiliza conhecimentos de matemática, estatística e ciência da computação, utilize seu tempo para focar nas camadas de cima da pirâmide, ou seja, para criar modelos de Machine Learning e auxiliar em tomadas de decisões, para responder às necessidades de negócio."""


texto2 = """O Trello é uma ferramenta que oferece um plano gratuito para organizar desde nossas tarefas pessoais até demandas coletivas de uma equipe. Ele possibilita que criemos quadros com listas e adicionemos nelas cartões – ou cards, como costumamos dizer no dia a dia – com itens e tarefas, que são úteis para organizar times e atividades específicas para um determinado conjunto de pessoas.

Uma grande vantagem do Trello para o trabalho em equipe são as atualizações colaborativas em tempo real. Então, se a Maria realizar uma mudança no quadro, todos os outros membros poderão acompanhar essa atualização de imediato. Tudo isso, apenas olhando o quadro, que mostra de forma resumida o andamento do projeto. Cada card também contém o histórico de alterações realizadas pelos membros.

Além disso, o Trello possui diversas funcionalidades para organização, como o uso de datas, lembretes e notificações para cartões de atividades, etiquetas, ingresso de membros, checklists e power-ups.

O Trello possui a grande vantagem de aceitar diferentes formas de anexo, onde você pode disponibilizar no card da sua tarefa diferentes documentos em vários formatos, seja ele pdf, mp4, png, dentre outros. Assim, todos do time conseguem ver os documentos envolvidos no projeto que você está trabalhando."""


# conta as chaves e mostra seus valores / retirando os maiúsculos com "lower"
Counter(texto1)
Counter(texto1.lower())


# dá nome ao contador
aparicoes = Counter(texto1.lower())
aparicoes


# soma e retorna a quantidade de valores que aparecem nas chaves
total_de_caracteres = sum(aparicoes.values())
total_de_caracteres


# conta a frequência com que as chaves aparecem, dividido pelo total de caracteres do texto
for letra, frequencia in aparicoes.items():
    tupla = (letra, frequencia / total_de_caracteres)
    print(tupla)


# também conta a frequência, mas escrito no formato "list comprehension"
proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
proporcoes


# cria um dicionário com os valores encontrados
proporcoes = dict(proporcoes)
proporcoes


# conta os caracteres que mais aparecem no texto e retorna os valores proporcionais
proporcoes = Counter(dict(proporcoes))
proporcoes.most_common(10)


# cria uma função que analisa e frequência e devolve sua proporção no texto
def analisa_frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres)
                  for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(caractere, "=>", proporcao)

analisa_frequencia_letras(texto1)


# formata os valores encontrados em porcentagem
def analisa_frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres)
                  for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_letras(texto1)
analisa_frequencia_letras(texto2)
