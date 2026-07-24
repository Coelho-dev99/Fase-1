def e_palindromo(palavra):
    palavra_invertida = palavra [::-1]

    if palavra == palavra_invertida:
        return True
    else:
        return False

palavra = input("Digite uma palavra:")

print(e_palindromo(palavra))
