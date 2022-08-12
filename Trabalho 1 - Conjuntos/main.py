# AFONSO ROCHA REKBAIM
'''
ENUNCIADO
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
ambiente repl.it quanto no ambiente Github.
Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
no mínimo um arquivo de testes criado pelo próprio professor. 
'''

file = open("teste1.txt")
content = file.readlines()
set1 = 2
set2 = 3
count = 0
oprList = 1


def union():
    union = []
    for i in range(len(listSet1)):
        union.append(listSet1[i])

    for i in range(len(listSet2)):
        if listSet2[i] not in union:
            union.append(listSet2[i])

    return union


def intersection():

    intersec = []
    for i in range(len(listSet1)):
        if listSet1[i] in listSet2:
            intersec.append(listSet1[i])

    return intersec


def difference():

    dif = []
    for i in range(len(listSet1)):
        if listSet1[i] not in listSet2:
            dif.append(listSet1[i])

    return dif


def cartesianProduct():
    crtPrd = [(x, y) for x in listSet1 for y in listSet2]
    return crtPrd


def format(result):
    if result == cartesianProduct():
        final = ', '.join(map(str, result))

    else:
        final = ', '.join(map(str, result))
      
    return final.replace("'", "").replace(" ", "").strip().replace(",", ", ")


def formatStatement():
    Set1 = ','.join(map(str, listSet1))
    Set2 = ','.join(map(str, listSet2))

    if opr.strip() == "U":
        print('União: conjunto 1 {',
              Set1.replace("'", "").strip().replace(",", ", "),
              '}, ',
              'conjunto 2 {',
              Set2.replace("'", "").strip().replace(",", ", "),
              '}',
              '. Resultado: {',
              format(union()),
              '}',
              sep="")

    elif opr.strip() == "I":
        print('Intercessão: conjunto 1 {',
              Set1.replace("'", "").strip().replace(",", ", "),
              '}, ',
              'conjunto 2 {',
              Set2.replace("'", "").strip().replace(",", ", "),
              '}',
              '. Resultado: {',
              format(intersection()),
              '}',
              sep="")

    elif opr.strip() == "D":
        print('Diferença: conjunto 1 {',
              Set1.replace("'", "").strip().replace(",", ", "),
              '}, ',
              'conjunto 2 {',
              Set2.replace("'", "").strip().replace(",", ", "),
              '}',
              '. Resultado: {',
              format(difference()),
              '}',
              sep="")

    else:
        print('Produto Cartesiano: conjunto 1 {', Set1.replace("'", "").strip().replace(",", ", "),'}, ','conjunto 2 {', Set2.replace("'", "").strip().replace(",", ", "), '}','. Resultado {', format(cartesianProduct()), '}',sep="")


while count < int(content[0]):

    opr = content[oprList]
    listSet1 = content[set1].replace('\n', "").strip().split(", ")
    listSet2 = content[set2].replace('\n', "").strip().split(", ")

    formatStatement()

    set1 += 3
    set2 += 3
    oprList += 3
    count += 1
  