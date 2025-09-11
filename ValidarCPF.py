cpf = "190.367.030-69" 
cpf_limpo = ""

#removendo caracteres especiais
for indice in range(len(cpf)):
    if cpf[indice] in '.-':
        continue
    else:
        cpf_limpo += cpf[indice]

#pegando os 9 primeiros dígitos
nove_digitos = cpf_limpo[:9]

#fazendo a multiplicação decrecesnte com 10 a cada caractere convertido em int, e somando tudo
numero10 = 10
digito_1 = 0
for digitos in range(len(nove_digitos)):
    conta_atual = int(nove_digitos[digitos]) * numero10
    digito_1 += conta_atual
    numero10 -= 1 

#multiplicando por 10 e fazendo o resto da divisão por 11, validando se for maior que 9 e zero
digito_1 = (digito_1 * 10) % 11
digito_1 = 0 if digito_1 > 9 else digito_1

dez_digitos = nove_digitos + str(digito_1)

#fazendo a multiplicação decrecesnte com 11 a cada caractere convertido em int, e somando tudo
numero11 = 11
digito_2 = 0
for digitos in range(len(dez_digitos)):
    digito_2 += int(dez_digitos[digitos]) * numero11
    numero11 -= 1

#multiplicando por 10 e fazendo o resto da divisão por 11, validando se for maior que 9 e zero
digito_2 = (digito_2 * 10) % 11
digito_2 = 0 if digito_2 > 9 else digito_2

#Os nove digitos mais os 2 ultimos
cpf_conferido = nove_digitos + str(digito_1) + str(digito_2)

#imprimindo resultado
if cpf_conferido == cpf_limpo:
    print(f"Resultado: {cpf_conferido}")
    print(f"Seu cpf de numero {cpf} e totalmente válido.")