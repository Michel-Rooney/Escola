num = int(input('Digite um número: '))
impares = [i for i in range(1, num+1) if num % 2 == 1]
s =0
for i in range(1, num+1):
    po = i - 1
    div = i / impares[po]

    s += div