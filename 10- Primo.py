def primo (n1):

    for divisor in range (2, n1):
        if n1 % divisor ==0:
            return print (f"O número {n1} não é primo")

    return print(f"O número {n1} é primo")

n1 = int( input("Digite um número: ") )

print(primo(n1))
