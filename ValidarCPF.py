
nove_digitos_com_ponto = "273.478.390-84" 
nove_digitos_limpo = ""

#removendo caracteres especiais
for indice in range(len(nove_digitos_com_ponto)):
    if nove_digitos_com_ponto[indice] in '.-':
        continue
    else:
        nove_digitos_limpo += nove_digitos_com_ponto[indice]

#pegando os 9 primeiros dígitos
nove_digitos = nove_digitos_limpo[:9]

#fazendo a multiplicação decrecesnte de 10 a cada caractere, e somando tudo
numero = 10
soma = 0
for digitos in range(len(nove_digitos)):
    conta_atual = int(nove_digitos[digitos]) * numero
    soma += conta_atual
    numero -= 1 

#multiplicando por 10 e fazendo o resto da divisão por 11, validando se for maior que 9 e zero
soma = (soma * 10) % 11
soma = 0 if soma > 9 else soma


