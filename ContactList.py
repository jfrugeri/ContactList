# lista que guarda todos os contatos
contatos = []

while True:
    nome = input('Qual o nome? ')
    idade = int(input('Digite a idade: '))
    numero = input('Digite o numero: ')
    # adiciona a tupla (nome, idade, numero) na lista de contatos
    contatos.append((nome, idade, numero))
    entrada = input("Deseja sair?\n")
    if entrada.lower() == "s":
        break # sai do while

maiores = []
menores = []
# separa os contatos por idade
for contato in contatos:
    if contato[1] >= 18:
        maiores.append(contato)
    else:
        menores.append(contato)

print(maiores)
print(menores)