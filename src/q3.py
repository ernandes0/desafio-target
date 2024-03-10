#A - adição de dois a cada novo elemento
sequencia_a = [1, 3, 5, 7]
proximo_elemento_a = sequencia_a[-1] + 2
print(proximo_elemento_a)
"O próximo elemento da sequência é 9."

#B - multiplicação por 2 de cada novo elemento
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_elemento_b = sequencia_b[-1] * 2
print(proximo_elemento_b)
"O próximo elemento da sequência é 128."

#C - Quadrado dos números
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_elemento_c = (len(sequencia_c))**2
print(proximo_elemento_c)
"O próximo elemento da sequência é 49."

#D - Quadrado dos números pares
sequencia_d = [4, 16, 36, 64]
proximo_elemento_d = (len(sequencia_d) * 2 + 2)**2
print(proximo_elemento_d)
"O próximo elemento da sequência é 100."

#E - Soma dos dois números anteriores(Fibonacci)
sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_elemento_e = sequencia_e[-1] + sequencia_e[-2]
print(proximo_elemento_e)
"O próximo elemento da sequência é 13."

#F - Números iniciados com a letra 'D'
proximo_elemento_f = 200
print(proximo_elemento_f)
"O próximo elemento da sequência é 200."