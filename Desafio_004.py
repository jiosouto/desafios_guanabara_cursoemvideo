algo = input('\033[97mDigite algo: ')
print('\033[34mÉ um número ou uma letra?\033[32m', algo.isalnum())
print('\033[34mÉ uma letra?\033[32m', algo.isalpha())
print('\033[34mÉ um digito?\033[32m', algo.isdigit())
print('\033[34mÉ algo em minúsculo?\033[32m', algo.islower())
print('\033[34mÉ algo decimal?\033[32m', algo.isdecimal())
print('\033[34mÉ um número?\033[32m', algo.isnumeric())
print('\033[34mÉ somente um espaço?\033[32m', algo.isspace())
print('\033[34mÉ algo em maiúsculo e minúsculo (Capitalizada)?\033[32m', algo.istitle())
print('\033[34mÉ algo em maiúsculo?\033[32m', algo.isupper())
