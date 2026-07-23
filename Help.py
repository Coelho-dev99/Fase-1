#tipos de dados#

#str (utilizado para dados em texto)
#int (Utilizado para dados de númericos inteiros)
#float (Utilizado para dados de númericos quebrados)
#boolean (Utilizado para true ou false)
#type (serve para mostrar o tipo do valor) exemplo: (type () ) - tudo que tiver dentro das "" é considero como str.

from os import remove

MATEMATICA#

# + (simbolo para função de soma)
# - (simbolo para função de subtração)
# * (Simbolo para função de multiplicação)
# / (Simbolo para função de divisão)
# ** (Simbolo para função de potencia)
# % (Simbolo para função de porcetagem)

print ("teste") # O comando print server para mostar na tela a mensagem que está dentro ("").

print (30+10) # Realiza função de soma 
print (30-10) # Realiza função de subtração
print (30*10) # Realiza função de multiplicação
print (30**10) # Realiza função de potência
print (30%10) # Realiza função de porcetagem (Ele me retorna o resto da divisão)

VARIÁVEIS#

primeiro_numero = 7 #Estou atribuindo o numero 7 a variável primeiro_numero
segundo_numero = 3 #Estou atribuindo o numero 3 a variável segundo_numero 

#Exemplo#

print (primeiro_numero + segundo_numero) # realiza a soma das duas variáveis que foram definidas acima.

resultado_soma = primeiro_numero + segundo_numero # Estou guardando o resultado da soma das duas variáveis em uma nova variável chamada resultado_soma

#Exemplo para nome#

nome ="Marcio"
print ("oi," + nome) # resoltara em "oi, Marcio" na tela, visto que a variável nome foi definida como Marcio.

INPUT#

#Exemplo#

nome =input ("Qual o seu nome? ") # com o "input" estou armazenando a resposta que será dada pela pergunta dentro do ("") e armazendo em "nome"

num1 = int (input ("Digite um número: ")) # Nesse exemplo estou definindo qual o tipo de dado será armazendo na variável num1, que nesse caso é int.

print ( f"O resultado da soma entre {num1} e {num2} é {resultado_soma} " ) # O "f" serve para formatar a mensagem, e as {} servem para mostrar o valor das variáveis.
#quando você coloca o f antes das aspas, o Python permite colocar variáveis dentro do texto usando chaves {}.#


CONDICIONAIS#

idade = int (input ("Qual a sua idade: ") ) 
    if idade > 17: # Se a condição for verdadeira, ou seja, se a idade for maior que 17, ele vai executar o comando abaixo.
        print (" Você e maior de idade")
    else: # Se a condição for falsa, ou seja, se a idade for menor que 17, ele vai executar o comando abaixo.
        print ("Você e menor de idade") 
    elif idade == 17: # Se a condição for verdadeira, ou seja, se a idade for igual a 17, ele vai executar o comando abaixo. (senão se)
        print ("Você tem 17 anos")

        #Em termos direto:
        if condição:# executa se a condição for verdadeira
        elif outra_condição: # executa se a condição acima for falsa
        else:# executa se todas as condições forem falsa


COLEÇÕES#
#Listas (utilizado para armazenar dados em uma lista)
#Listas são representadas por colchetes [] e os valores são separados por vírgula.

Frutas = ["maça", "banana", "laranja"] # Estou criando uma lista chamada frutas, e dentro dela estou armazenando 3 valores.
print (Frutas) # Vai mostrar na tela a lista completa.
print (Frutas [1]) # Vai mostrar na tela o valor que está na posição 1 da lista, que nesse caso é banana. (Lembrando que a contagem começa do 0)

frutas [1] = "abacaxi" # Estou substituindo o valor que está na posição 1 da lista, que nesse caso é banana, por abacaxi.
print (frutas) # Vai mostrar na tela a lista completa, mas agora com o valor abacaxi no lugar de banana.

frutas.append ("melancia") # Estou adicionando um novo valor na lista, que nesse caso é melancia. 
append # é uma função que serve para adicionar um novo valor na lista. (append significa adicionar)
print (frutas) # Vai mostrar na tela a lista completa, agora com o valor melancia

frutas.insert (1, "morango") # Estou adicionando um novo valor na lista, que nesse caso é morango, na posição 1 da lista. (insert significa inserir)
insert # é uma função que serve para adicionar um novo valor na lista, em uma posição específica.
print (frutas) # Vai mostrar na tela a lista completa, agora com o valor morango na posição 1 da lista.

frutas.remove ("banana") # Estou removendo o valor banana da lista. (remove significa remover)
remove # é uma função que serve para remover um valor da lista.
print (frutas) # Vai mostrar na tela a lista completa, agora sem o valor banana.


#tuplas (utilizado para armazenar dados em uma tupla)
#Tuplas são representadas por parenteses () e os valores são separados por vírgula e não pode ser alterado depois de criado.

cores = ("vermelho", "azul", "verde") # Estou criando uma tupla chamada cores, e dentro dela estou armazenando 3 valores.
cores [1] = "amarelo" # Estou tentando substituir o valor que está na posição 1 da tupla, que nesse caso é azul, por amarelo. (Isso não é permitido, pois tuplas são imutáveis)

#Exemplo# 

minha_tupla = [("maça", "banana"), ("verde", "azul")] # Estou criando uma tupla dentro de uma lista, e dentro da tupla estou armazenando 2 valores. 
print (minha_tupla [1] [0]) # Vai mostrar na tela o valor que está na posição 1 da lista, que nesse caso é a tupla ("verde", "azul"), e dentro da tupla ele vai mostrar o valor que está na posição 0, que nesse caso é verde.

DICIONÁRIOS#
#Dicionários são representados por chaves {} e os valores são armazenados em pares de chave:valor, separados por vírgula.

dados = {"nome": "Marcio", "idade": 30, "cidade": "Brasilia"} # Estou criando um dicionário chamado dados, e dentro dele estou armazenando 3 pares de chave:valor.
print (dados) # Vai mostrar na tela o dicionário completo.  
print (dados ["nome"]) # Vai mostrar na tela o valor que está na chave "nome", que nesse caso é Marcio.]
dados ["cidade"] = "São Paulo" # Estou substituindo o valor que está na chave "cidade", que nesse caso é Brasilia, por São Paulo.

LOOP#

#while (enquanto) - é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.
#for (para) - é uma estrutura de repetição que executa um bloco de código um número determinado de vezes.

contador = 10 #Exemplo para while, estou criando uma variável chamada contador e atribuindo o valor 10 a ela.
while contador >=1: # Enquanto a condição for verdadeira, ele vai executar o bloco de código abaixo.
    print (f"contagem atual: {contador}") # Vai mostrar na tela a contagem atual, que nesse caso é o valor da variável contador.
    contador -= 1 # Estou diminuindo o valor da variável contador em 1 a cada)

    senha = "calma"
    tentativa_senha = ""
    while senha != tentativa_senha: # Enquanto a senha for diferente do valor digitado, ele vai executar o bloco de código abaixo.
        tentativa_senha = input ("digite a senha: ") 
        if tentativa_senha != senha: # se a senha digitada for diferente da senha correta, ele vai executar o print logo a baixo
            print ("senha incorreta, tente novamente")
        else:
            print ("senha correta, acesso permitido")

compras =["maça", "banana", "laranja"] #Exemplo para for, estou criando uma lista chamada compras e armazenando 3 valores dentro dela.
for item in compras: # O for vai percorrer cada item da lista compras, e a cada iteração ele vai armazenar o valor do item na variável item.
    print (f "Voce precisar comprar o seguinte item: {item}") # Vai mostrar na tela a mensagem "Voce precisar comprar o seguinte item: " e o valor da variável item, que nesse caso é o valor da lista compras.

numeros = [5, 3, 5, 6 ,1, 9, 3, 5, 8] # Estou criando uma lista chamada numeros e armazenando 9 valores dentro dela.]
for numero in numeros:
    if numero % 2 ==0:
        break # Se o número for par, ele vai executar o comando break, que vai interromper o loop e sair do bloco de código.
        continue # Se o número for ímpar, ele vai executar o comando continue, que vai pular para a próxima iteração do loop e continuar executando o bloco de código.


FUNÇOES#

#def (definir) - é uma palavra reservada do Python que serve para definir uma função.

def olá(nome): # Estou criando uma função chamada olá, que vai receber um parâmetro chamado nome.
    print(f"Olá, {nome}!") # Vai mostrar na tela a mensagem "Olá, " e o valor do parâmetro nome.
inserir_nome = input ("Digite o seu nome: ") # Estou armazenando o valor digitado pelo usuário na variável inserir_nome.
olá(inserir_nome) # Estou chamando a função olá e passando o valor da variável inserir_nome como parâmetro.


def somar(n1, n2): # Estou criando uma função chamada somar, que vai receber dois parâmetros chamados n1 e n2.
    resultado = n1 + n2 # Estou armazenando o resultado da soma dos parâmetros n1 e n2 na variável resultado.
    return resultado # Estou retornando o valor da variável resultado para quem chamou a função.

#return é uma palavra reservada do Python que serve para retornar um valor de uma função para quem chamou a função.
 
resultado_da_soma = somar (5, 10) # Estou chamando a função somar e passando os valores 5 e 10 como parâmetros, e armazenando o valor retornado na variável resultado.
print (f"O resultado da soma é: {resultado_da_soma}") # Vai mostrar na tela a mensagem "O resultado da soma é: " e o valor da variável resultado, que nesse caso é 15.

MODULOS#

# Modulos são basciammente utilizar arquvios criados dentro da workspace, para reutilizar funções, variáveis e etc.

#Exemplo#

import Tabuada # estou importante o arquvio tabuada.py, que está dentro da minha workspace, para poder utilizar as funções dela, (utilizando exemplo das funções criadas acima)

funcoes.olá("marcio") # Estou chamando a função olá, que está dentro do arquivo tabuada.py, e passando o valor "marcio" como parâmetro.

from funcoes import somar # estou importando a função somar, que está dentro do arquivo tabuada.py, para poder utilizar ela sem precisar chamar o arquivo todo.
from funcoes import somar, olá # estou importando as funções somar e olá, que estão dentro do arquivo tabuada.py, para poder utilizar elas sem precisar chamar o arquivo todo.
from funcoes import * # estou importando todas as funções, que estão dentro do arquivo tabuada.py, para poder utilizar elas sem precisar chamar o arquivo todo.


somar (5, 10) # Estou chamando a função somar, que está dentro do arquivo tabuada.py, e passando os valores 5 e 10 como parâmetros.
olá ("marcio") # Estou chamando as funções somar e olá, que estão dentro do arquivo tabuada.py, e passando os valores 5 e 10 como parâmetros para a função somar, e o valor "marcio" como parâmetro para a função olá.


BIBLOTECA#

#Bibliotecas são basciammente utilizar arquvios criados dentro da workspace, para reutilizar funções, variáveis e etc.
