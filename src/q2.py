def pertence_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if pertence_fibonacci(numero_informado):
    print(f"{numero_informado} está presente na sequência de Fibonacci.")
else:
    print(f"{numero_informado} não está presente na sequência de Fibonacci.")
