frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

if frase == "":
    print("A frase está vazia.")
else:
    contador = 0
    for caractere in frase:
        if caractere in vogais:
            contador += 1
    print(f"A frase contém {contador} vogais.")
