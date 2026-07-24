lista = []

while True:
    numero = int(input ("Digite um número: ") )
    lista.append (numero)

    continuar = input ("Deseja adicionar mais um número? (s/n): ")
    if continuar == "n":
        break

lista_sem_duplicados = []

for numero in lista:
    if numero not in lista_sem_duplicados:
        lista_sem_duplicados.append(numero)

print (f"A sua lista digitada é: {lista}")
print (f"A lista sem elementos duplicados é: {lista_sem_duplicados}")   
