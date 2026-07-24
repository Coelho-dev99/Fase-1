lista =[]

while True:
    numero = int (input("Digite um número: ") )
    lista.append (numero)

    continuar = input ("Deseja adicionar mais um número? (s/n): ")
    if continuar == "n":
        break

maior = lista [0]

for numero in lista:
    if numero  > maior:
        maior = numero

print (f"A sua lista digitada é: {lista}")
print (f"O maior número da sua lista é: {maior}")
