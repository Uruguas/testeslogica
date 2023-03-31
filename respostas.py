'''
 Teste Ribeirão preto.
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);


1) O valor da Variavel SOMA sera 1. (Codigo abaixo)
'''
indicie = 13
soma = 0 
k = 0

if k < indicie:
    k = k + 1
    soma = soma + k
print(soma)

'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência.

'''
numero_recebido = int(input('Digite um numero para saber se pertence a sequència de Fibonacci: '))

x, y  = 0, 1

while y < numero_recebido:
    x, y = y, x + y
    
if y == numero_recebido:
    print(f'{numero_recebido} pertence á sequencia de Fibonacci.')
else:
    print(f'{numero_recebido} não pertence a sequência de Fibonacci')
     
''' 
3) Encontre a Logica

a) 1, 3, 5, 7, 9 (Adicionar 2)
b) 2, 4, 8, 16, 32, 64, 128 (Multiplicar vezes 2)
c) 0, 1, 4, 9, 16, 25, 36, 49 (Numeros ao quadrado, 1 ao quadrado, 2, 3, 4...  )
d) 4, 16, 36, 64, 100 (Soma 8 a diferença entre a subtração do numero com o numero anterior, e depois soma o valor da subtração + o numero)
e) 1, 1, 2, 3, 5, 8, 13 (Sequencia de Fibonacci)
f) 2, 10, 12, 17, 18, 19, 200 (São os numeros que começam com a letra D (Foi a mais dificil :) )) 

''' 


'''
4) Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto
a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?


Resposta:
Eles se encontram a mesma distancia.
A distancia entre uma cidade e outra e de 100km, e no momento que eles se cruzarem, eles vão se encontrar a mesma distancia de Riberião preto, 
independente do tempo que cada um demora para percorrer o trajeto.

'''

'''

5) Escreva um programa que inverta os caracteres de uma string

'''
s = str(input('Digite uma frase: '))
s_invertida = s[::-1]
print(s_invertida)