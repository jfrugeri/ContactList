# lista que guarda todos os contatos
contatos = []

while True:
    nome = input('Qual o nome? ')
    idade = int(input('Digite a idade: '))
    numero = input('Digite o numero: ')
    # adiciona a tupla (nome, idade, numero) na lista de contatos
    contatos.append((nome, idade, numero))
    entrada = input("Deseja sair? sim(s) nao(n)\n")
    if entrada.lower() == "s":
        break # sai do while

lista1 = []
lista2 = []
# separa os contatos por idade
for contato in contatos:
    if contato[1] >= 18:
        lista1.append(contato)
    else:
        lista2.append(contato)

print(lista1)
print(lista2)