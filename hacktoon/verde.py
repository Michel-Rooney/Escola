num, n1, n2 = int(input('Digite um número: ')), 0, 1


for i in range(0, num):
    n3 = n1 + n2
    if n3 > num:
        print('O número não está na sequencia')
        break
    if num == n3:
        print('O número está na sequencia') 
        break
    n1 = n2
    n2 = n3   
else:    
    print('O número não está na sequencia')