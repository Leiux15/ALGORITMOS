valor = float(input('\nDigite o valor da prestação: '))
taxa = float(input('\nDigite a taxa: '))
tempo = float(input('\nDigite o tempo (Número de meses): '))
prest = valor + (valor * (taxa / 100) * tempo)

print(f'\nO valor da prestacao em atraso é {prest}')
print('\n')