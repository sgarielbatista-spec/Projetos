import random

quantidade_cpf = input("Digite quantos cpf quer:")
try:
    quantidade_cpf = int(quantidade_cpf)
    for _ in range(quantidade_cpf):

        cpf = ''
        for i in range(9):
            cpf += str(random.randint(0, 9))

        #pegando os 9 primeiros dígitos
        nove_digitos = cpf[:9]

        #fazendo a multiplicação decrescente com 10 a cada caractere convertido em int, e somando tudo
        digito_1 = 0
        for i, digitos in enumerate(nove_digitos):
            digito_1 += int(digitos) * (10 - i)


        #multiplicando por 10 e fazendo o resto da divisão por 11, validando se for maior que 9 e zero
        digito_1 = (digito_1 * 10) % 11
        digito_1 = 0 if digito_1 > 9 else digito_1

        dez_digitos = nove_digitos + str(digito_1)

        #fazendo a multiplicação decrescente com 11 a cada caractere convertido em int, e somando tudo
        digito_2 = 0
        for i, digitos in enumerate(dez_digitos):
            digito_2 += int(digitos) * (11 - i)

        #multiplicando por 10 e fazendo o resto da divisão por 11, validando se for maior que 9 e zero
        digito_2 = (digito_2 * 10) % 11
        digito_2 = 0 if digito_2 > 9 else digito_2

        #Os nove digitos mais os 2 ultimos
        cpf_conferido = nove_digitos + str(digito_1) + str(digito_2)

        #imprimindo resultado
        print(f"Resultado: {cpf_conferido}")
except ValueError:
    print("Digite um número")


