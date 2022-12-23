from datetime import date

nome = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
ctps = int(input('Carteira de Trabalho - 0 caso não possua: '))
if ctps != 0:
    contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
cadastro = {'Nome': nome,
            'Nascimento': nascimento,
            'Idade': idade,
            'CTPS': ctps,
            'Ano de contratação': (contratacao if ctps != 0 else 0000),
            'Salário': (salario if ctps != 0 else 0000.00),
            'Aposentadoria em': (contratacao+15 if ctps != 0 else 0000)}
print('-='*20)
for k, v in cadastro.items():
    print(f'{k}: {v}')