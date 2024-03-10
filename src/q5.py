def inverter_string(input_string):
    caracteres = list(input_string)
    inicio, fim = 0, len(caracteres) - 1

    while inicio < fim:
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        inicio += 1
        fim -= 1
    string_invertida = ''.join(caracteres)
    return string_invertida

entrada = input("Digite uma string: ")
resultado = inverter_string(entrada)

print(f'A string invertida é: {resultado}')
