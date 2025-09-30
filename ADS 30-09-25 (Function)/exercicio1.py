#Julia é professora e precisa de um programa para ajudar
#seus alunos a calcularem suas idades com base no ano de
#nascimento. Sua tarefa é criar uma função que receba o ano
#de nascimento e o ano atual e retorne à idade
#correspondente.

nascimento = int(input("Coloque sua ano de nascimento:"))
atual = int(input("Coloque o ano atual:"))

def calculador(nascimento, atual):
    resultado =  (atual - nascimento)
    return resultado

print({calculador(nascimento, atual)})