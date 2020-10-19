## List
L1=[] # Cria 1 lista vazia ou "L1=list()"
for ii in range(5,8+1): L1.append(ii) # faz um loop de 5 a 8 e inclui cada n° no fim da lista
print(L1) # Imprime todos os elementos da lista
L1=list(range(5,8+1)) # Forma condensada para fazer o que foi feito acima
print(L1) # Imprime todos os elementos da lista
L1=[5,6,7,8]     # Definindo manualmente a mesma lista acima
print(L1.index(5), L1.index(6), L1.index(7), L1.index(8)) # Retorna o indice de um dado elemento
print(L1.index(15)) # Erro pois o L1 não tem o elemento 15.
print(L1[0],L1[1],L1[2],L1[3]) # Imprime elemento a elemento
for d in L1: print(d) # Imprime todos os elementos (igual acima)
for ii,d in enumerate(L1): print(ii,d) # Imprime todos os elementos com o indice deles
for ii in range(len(L1)): print(ii,L1[ii]) # Imprime todos os elementos com o indice deles
print(L1[0],L1[1],L1[2],L1[3],L1[4]) # Erro: lista não tem o indice 4

L1=["a","b","c", "ed"] # Lista de letras (caracteres ou string)
print(L1[0],L1[1],L1[2],L1[3]) # Imprime elemento a elemento
for d in L1: print(d) # Imprime todos os elementos (igual acima)
for ii,d in enumerate(L1): print(ii,d) # Imprime todos os elementos com o indice deles
print(L1[0],L1[1],L1[2],L1[3],L1[4]) # list index out of range



## Join (usado p/ string = sequencia de caracteres)
L1=["a","b","c", "ed"] # Lista de letras
print(" ".join(L1)) # Imprime todos os elementos "sem usar um Loop"
L1=[5,6,7,8]     # Lista de número
print(" ".join(L1)) #Erro: Os elementos da lista tem que ser string (caracteres)
for ii in range(len(L1)): L1[ii]=str(L1[ii]) # Converte cada num. para string (caracteres)
print(" ".join(L1)) # Imprime todos os elementos



## List Slice => Data[Inicio:Fim:Passo]
Data=list(range(-10,10)) # Cria uma lista [-10, -9, ..., 8, 9]
print(Data[3:12:2]) # imprime de dois em dois os elementos com indice entre 3 e 12
print(Data[:-1:])   # imprime todos os elementos menos o último
print(Data[::-1])   # imprime todos os elementos em ordem reversa
print(Data[5::])    # imprime todos os elementos com indice >= 5
print(Data[-5::])   # imprime os últimos 5 elementos na ordem q aparecem


## Function
def GreatThanZeroV1(Value): # Defini uma função
    return Value > 0
def GreatThanZeroV2(Value): # Defini outra função
    print(Value > 0)
Data=list(range(-10,10)) # Cria uma lista [-10, -9, ..., 8, 9]
for ii in range(len(Data)):
    print( GreatThanZeroV1(Data[ii]) ) # Imprime TRUE ou FALSE para cada elemento da lista
for d in Data:
    print( GreatThanZeroV1(d) ) # Imprime TRUE ou FALSE para cada elemento da lista
for ii in range(len(Data)):
    GreatThanZeroV2(Data[ii]) # Imprime TRUE ou FALSE para cada elemento da lista
for d in Data:
    GreatThanZeroV2(d) # Imprime TRUE ou FALSE para cada elemento da lista


## Lambda (é uma função anônima)
GTZLambdaA=lambda x: x>0 # Cria 1 função lambda
print( GTZLambdaA(10) ) # Imprime TRUE ou FALSE
print( GTZLambdaA(-5) ) # Imprime TRUE ou FALSE
GTZLambdaB=lambda x: print(x>0) # Cria 1 função lambda
GTZLambdaB(10) # Imprime TRUE ou FALSE
GTZLambdaB(-5) # Imprime TRUE ou FALSE
Data=list(range(-10,10)) # Cria uma lista [-10, -9, ..., 8, 9]
for d in Data:
    print(GTZLambdaA(d)) # Imprime TRUE ou FALSE para cada elemento da lista
for d in Data:
    GTZLambdaB(d) # Imprime TRUE ou FALSE para cada elemento da lista



## Map
GTZLambdaA=lambda x: x>0 # Cria 1 função lambda
Data=list(range(-10,10)) # Cria uma lista [-10, -9, ..., 8, 9]
print(list(map(GTZLambdaA, Data))) # Usando MAP para subtituir o Loop For



## Filter
GTZLambdaA=lambda x: x>0 # Cria 1 função lambda
Data=list(range(-10,10)) # Cria uma lista [-10, -9, ..., 8, 9]
print(Data)
print(list(filter(GTZLambdaA, Data))) # cria 1 nova lista com os elementos >0 da lista Data



## List Comprehension
L1=[] # Cria 1 lista vazia ou "L1=list()"
for ii in range(5,8+1): L1.append(ii) # faz um loop de 5 a 8 e inclui cada n° no fim da lista
print(L1)
L1=[ii for ii in range(5,8+1)] # Escrevendo o for Loop na forma comprimida
print(L1)
L1=list(range(5,8+1)) # mais comprimido ainda
print(L1)

print(" ".join(L1)) #Erro: Os elementos da lista tem que ser string (caracteres)
L1=[str(ii) for ii in range(5,8+1)] # Vamos converter usando compressao
print(L1)
print(" ".join(L1)) # Imprime todos os elementos

L1=[ii for ii in range(5,8+1)] # Escrevendo o for Loop na forma comprimida
print(list(map(str,L1))) # ou podemos converter usando map e imprimir tudo (sem usar Loop for)



## Input
n=input() # se digitar 1 e deter entrer, n vai ser uma letra ('1')
print(n)
print(n+1) # vai dar erro, n é uma letra e não tem como somar uma letra com um número.
n=int(input()) # se digitar 1 e deter entrer, n vai ser o número 1
print(n)
print(n+1) # agora vai dar certo, n é um número.
n=input() # se digitar 1 2 3 4 e deter entrer, n vai ser uma sequencia de letras ('1 2 3 4')
print(n)
# se quiser armazenar cada elemento separadamente, vc tem que "dividir" a entrada, neste caso, usando o espaço como separador, veja:
n=input().split(" ") #se digitar 1 2 3 4 e deter entrer, n vai ser uma lista de letras (['1', '2', '3', '4'])
print(n)
# se quiser armazenar cada elemento como int, temos q converter
n=list(map(int,input().split(" "))) #se digitar 1 2 3 4 e deter entrer, n vai ser uma lista de números INTEIROS ou INT ([1, 2, 3, 4])
print(n)
n=list(map(float,input().split(" "))) #se digitar 1 2 3 4 e deter entrer, n vai ser uma lista de números REAIS ou FLOAT ([1.0, 2.0, 3.0, 4.0])
print(n)
# podemos fazer a mesma coisa usando o stdin da biblioteca sys
from sys import stdin
n=list(map(int, stdin.readline().split(" ") )) # troquei o input pelo stdin (geralmente é mais rápido)



## Lists of Lists
L1=[0]*5 # Cria um vetor linha (1D) com 5 colunas, todas com zero
print(L1)
L1=[0 for ii in range(5)] # podemos fazer desta forma tbm
print(L1)
L1=[] # Criando uma lista vazia para nosso vertor 2D
for ii in range(5): # Criando um vetor 2D (5 x 5), com tudo Zero
    L1.append([])
    for jj in range(5):
        L1[ii].append(0)
print(L1)
L1=[[0]*5 for ii in range(5)] # Criando um vetor 2D (5 x 5), com tudo Zero (forma condensada)
print(L1)
print(L1[4][4]) # acessando a última posição do vetor, usando os indices de linha e coluna (4 e 4)
for linha in L1: # imprimindo cada elemento do vetor 2D
    for elemento in linha:
        print(elemento, "",end="", sep=" ") # explicar que no final de cada linha terá um espaço extra....
    print("")
L1=[] # Criando uma lista vazia para nosso vertor 2D
for ii in range(5): # Criando um vetor 2D (5 x 5), com numeros sequenciais
    L1.append([])
    for jj in range(5):
        L1[ii].append( (ii*5)+jj )
print(L1)
# Slice da Matriz 2D (lists of Lists)
print(L1[:-1:])     # imprime todas as linhas da matriz menos a última
print(L1[::-1])     # imprime todas as linhas da matriz em ordem reversa
print(L1[2::])      # imprime as linhas da matriz com indice >= 2
print(L1[-2::])     # imprime as linhas últimas 2 linhas da matrizos na ordem q aparecem
# lists of Lists => Slice não funciona na vertical, não nativamente (ex. pegar todos os elementos da primeira coluna). (Vamos fazer isso com o numpy)



## Numpy ## python -m pip install numpy
import numpy as np
L1=list(range(0,25)) # Cria uma lista de 0 a 24
print(type(L1)) # verifica o tipo de dados da variável L1 <class 'list'>
print(L1) # Imprime os elementos da lista
L1=np.array(L1) # converte a lista para usar o numpy
print(type(L1))  # verifica o tipo de dados da variável L1 <class 'numpy.ndarray'>
print(L1) # Imprime os elementos da lista
L1=L1.reshape((5,5)) # Criando um vetor 2D (5 x 5), com numeros sequenciais (igual fizemos no tópico anterior, mas bem mais simples)
print(L1) # Imprime a matriz 2D (5 x 5)
print(L1.shape) # imprime a qtde de linhas e colunas da matriz
# Slice com numpy L1[ Linha, Coluna ] onde:
#                      Linha = Inicio:Fim:Passo
#                      Colune= Inicio:Fim:Passo
print(L1[0:1:, :: ])    # imprime os elementos da primeira linha
print(L1[1:2:, :: ])    # imprime os elementos da segunda linha
print(L1[0:2:, :: ])    # imprime os elementos da primeira e segunda linha
print(L1[::, 0:1: ])    # imprime os elementos da primeira coluna
print(L1[::, 1:2: ])    # imprime os elementos da segunda coluna
print(L1[::, 0:2: ])    # imprime os elementos da primeira e segunda coluna
print(L1[0:1:, ::-1 ])  # imprime os elementos da primeira linha em ordem reversa
print(L1[1:2:, ::-1 ])  # imprime os elementos da segunda linha em ordem reversa
print(L1[0:2:, ::-1 ])  # imprime os elementos da primeira e segunda em ordem reversa
print(L1[::-1, 0:1: ])  # imprime os elementos da primeira coluna em ordem reversa
print(L1[::-1, 1:2: ])  # imprime os elementos da segunda coluna em ordem reversa
print(L1[::-1, 0:2: ])  # imprime os elementos da primeira e segunda coluna em ordem reversa
print(L1[0:1:, ::-2 ])  # imprime os elementos da primeira linha em ordem reversa e de dois em dois
print(L1[1:2:, ::-2 ])  # imprime os elementos da segunda linha em ordem reversa e de dois em dois
print(L1[0:2:, ::-2 ])  # imprime os elementos da primeira e segunda em ordem reversa e de dois em dois
print(L1[::-2, 0:1: ])  # imprime os elementos da primeira coluna em ordem reversa e de dois em dois
print(L1[::-2, 1:2: ])  # imprime os elementos da segunda coluna em ordem reversa e de dois em dois
print(L1[::-2, 0:2: ])  # imprime os elementos da primeira e segunda coluna em ordem reversa e de dois em dois
print(L1[0:1:, ::2 ])   # imprime os elementos da primeira linha de dois em dois
print(L1[1:2:, ::2 ])   # imprime os elementos da segunda linha de dois em dois
print(L1[0:2:, ::2 ])   # imprime os elementos da primeira e segunda de dois em dois
print(L1[::2, 0:1: ])   # imprime os elementos da primeira coluna de dois em dois
print(L1[::2, 1:2: ])   # imprime os elementos da segunda coluna de dois em dois
print(L1[::2, 0:2: ])   # imprime os elementos da primeira e segunda coluna de dois em dois
print(L1[1:4:, 1:4: ])  # imprime os elementos internos (descarta a primera e a última linha, a primera e a última coluna) 
print(L1[0:1:, :: ].sum())    # imprime a soma dos elementos da primeira linha
print(L1[0:2:, :: ].sum())    # imprime a soma dos elementos da primeira e segunda linha


# ZIP => aggregate elements from two or more iterables => TWO range:
for ii, jj in zip(range(0,5), range(5,0,-1)): 
    print(ii, jj)
print(L1)
for ii, jj in zip(range(0,L1.shape[0]), range(L1.shape[1],0,-1)): # pega os elementos acima da diagnomal secundária (incluindo eles)
    print(L1[ii, 0:jj])


print([L1[ii,ii] for ii in range(5)]) # Imprime os elementos da diagonal principal

L1[1:4:, 1:4: ]=0  # coloca ZERO nos elementos internos 
print(L1)

L1=np.ones((5,5)) #Cria um vetor de uns (5 x 5)
print(L1) # Imprime os elementos
L1=np.zeros((5,5)) #Cria um vetor de zeros (5 x 5)
print(L1) # Imprime os elementos

Mat1=np.array([ [1,2,3], [4,5,6] ])
Mat2=np.array([ [9,8,7], [6,5,5] ])
print(Mat1)
print(Mat2)
print(Mat1 * Mat2) # multiplica os elementos das matrizes com seus correspondentes

Mat1=np.array([ [1,2,3], [4,5,6] ])
Mat2=np.array([9,8,7])
print(Mat1)
print(Mat2)
print(Mat1.dot(Mat2)) # realiza a multiplicação das matrizes


## Na maratona o comando "import numpy as np" vai dar erro.
## Isso porque numpy é um biblioteca externa ao python por isso instalamos ela com "python -m pip install numpy"
## Para usar essa estrutura do numpy, temos que embarcar ele no código
## Assim,vamos usar o arquivo "TinyNumpyBase.py" como base para embarcar (https://github.com/eldereng/MaratonaProgramacao2020-Matriz/)
## Mostrar como embardar o numpy, basicamente incluir seu código dentro de "def mainCode():", testar e enviar o arquivo no URI...
## Veja o arquivo "TinyNumpyExample.py", nele mostramos as operações acima sem usar a biblioteca numpy.
##    python TinyNumpyExample.py