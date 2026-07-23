Numero1 = float (input (" Digite o primeiro número: ") )
Numero2 = float (input (" Digite o segundo número: ") )

operação = input ("Digite a operação desejada ( + , - , * , / , ** , % ):")

if operação == "+":
    resultado = Numero1 + Numero2
    print ("O resultado da soma é: ", resultado)
elif operação == "-":
    resultado = Numero1 - Numero2
    print ("O resultado da subtração é: ", resultado)
elif operação == "*":
    resultado = Numero1 * Numero2
    print ("O resultado da multiplicação é: ", resultado)
elif operação == "/":
    resultado = Numero1 / Numero2
    print ("O resultado da divisão é: ", resultado)
elif operação == "**":
    resultado = Numero1 ** Numero2
    print ("O resultado da potência é: ", resultado)
elif operação == "%":
    resultado = Numero1 % Numero2
    print ("O resultado do módulo é: ", resultado)
else:
    print ("Operação inválida!")
