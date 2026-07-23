numero =int (input ("Digite um número para a tabuada: ") )
limite = int (input ("Digite até onde a tabuada deve ir: ") )

for i in range (1, limite + 1):
    resultado = numero * i
    print (numero, "x", i, "=", resultado)
