import matplotlib.pyplot as plt

qtd_de_alunos = int(input("Digite a quantidade de alunos: "))
print("\n")
alunos = [str(input("Digite o nome do aluno e aperta enter: ")) for i in range(qtd_de_alunos)]
prova1 = [float(input("Digite as notas da P1 (ou negativo pra falta) na ordem dos nomes: ")) for i in range(qtd_de_alunos)]
prova2 = [float(input("Digite as notas da P2 (ou negativo pra falta) na ordem dos nomes: ")) for i in range(qtd_de_alunos)]

reprovados = 0
aprovados = 0
recuperacao = 0
for i in range(qtd_de_alunos):
    if prova1[i] < 0 and prova2[i] <0:
        reprovados += 1
        print(alunos[i], 'Reprovado')
    elif prova1[i] <0 or prova2[i] <0:
        print(alunos[i], 'Precisa fazer Segunda Chamada')
    else:    
        media_aluno = (prova1[i] + prova2[i])/2    
        if media_aluno >= 7:
            aprovados += 1
            print(alunos[i], media_aluno, 'Aprovado')
        elif media_aluno < 5:
            reprovados += 1
            print(alunos[i], media_aluno, 'Reprovado')
        else:
            recuperacao += 1
            print(alunos[i], media_aluno, 'Recuperação')

falta_p1 = 0
falta_p2 = 0
soma_p1 = 0
soma_p2 = 0
for i in range(qtd_de_alunos):
    if prova1[i] < 0:
        falta_p1 += 1
    if prova2[i] < 0:
        falta_p2 += 1
    if prova1[i] >= 0:
        soma_p1 += prova1[i]
    if prova2[i] >= 0:
        soma_p2 += prova2[i]

media_p1 = soma_p1/(qtd_de_alunos - falta_p1)    
media_p2 = soma_p2/(qtd_de_alunos - falta_p2)
print('Média da Prova 1:', media_p1)
print('Média da Prova 2:', media_p2)

p1 = list(filter(lambda x: x > 0, prova1))
p2 = list(filter(lambda x: x > 0, prova2))

fig, axs = plt.subplots()
axs.hist(p1, label = 'Prova 1')
axs.set_title('Notas')
plt.show()

fig, axs = plt.subplots()
axs.hist(p2, label = 'Prova 2')
axs.set_title('Notas')
plt.show()

fig1, ax1 = plt.subplots()
ax1.pie([reprovados, aprovados, recuperacao], labels = ['Reprovados', 'Aprovados', 'Recuperação'], autopct= '%1.1f%%', startangle= 90)
ax1.axis('equal')
plt.show()
