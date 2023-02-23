nome = str(input('Digite o nome do atleta: '))
lista_salto = []

for i in range(1, 6):
    salto = float(input(f'{i}º Salto: '))
    lista_salto.append(salto)
    

maior = max(lista_salto)
menor = min(lista_salto)
print(f'O maior é {maior}')
print(f'O menor é {menor}')

lista_salto.remove(maior)
lista_salto.remove(menor)

media = sum(lista_salto) / len(lista_salto)
print(f'{nome}: {media}')



