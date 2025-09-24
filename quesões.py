import os
perguntas = [
    {
        "pergunta": "Quanto é 2+2?",
        "opções": ["1", "2", "3", "4"],
        "resposta": "4",
    }, 
    {
        "pergunta": "Quanto é 5*5?",
        "opções": ["25", "30", "50", "20"],
        "resposta": "25",
    },
    {
        "pergunta": "Qual a idade de maioridades no Japão?",
        "opções": ["16", "23", "20", "21"],
        "resposta": "20",
    }
]
lista_correcao = []
numero_questoes_certas = 0
for q in range(len(perguntas)):
    print(perguntas[q]["pergunta"])

    for indice, valor in enumerate(perguntas[q]["opções"]):
        print(f"{indice}){valor}")
    try:
        resposta = int(input("reponda: "))
        if perguntas[q]['opções'][resposta] == perguntas[q]["resposta"]:
            lista_correcao.append(True)
            numero_questoes_certas += 1
        else:
            lista_correcao.append(False)
    except (ValueError, IndexError):
        lista_correcao.append(False)
        continue
os.system("cls")

print(f"Você acertou {numero_questoes_certas} questões.")
print(f"Você acertou as questões")

for i, valor in enumerate(lista_correcao):
    if valor:
        print(perguntas[i]["pergunta"])
    