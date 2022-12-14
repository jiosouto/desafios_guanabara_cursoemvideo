objeto1 = objeto2 = objeto3 = objeto4 = 0
print('='*50)
print('{: ^50}'.format('BANCO PAN'))
print('='*50)

valor = int(input('Que valor você quer sacar? R$ '))

objeto1 = valor // 50
valor1 = objeto1*50
if valor1 < valor:
    objeto2 = (valor - valor1) // 20
    valor2 = objeto2*20
    if (valor1 + valor2) < valor:
        objeto3 = (valor - valor1 - valor2) // 10
        valor3 = objeto3*10
        if (valor1 + valor2 + valor3) < valor:
            teste_final = (valor1 + valor2 + valor3)
            objeto4 = valor - teste_final

print(f'''Total de {objeto1} cédulas de R$50.
Total de {objeto2} cédulas de R$20.
Total de {objeto3} cédulas de R$10.
Total de {objeto4} cédulas de R$1.''')
print('='*50)
print('Volte sempre ao BANCO GABRIEL! Tenha um bom dia!')
print('='*50)