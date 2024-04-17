cpf = '01444695614'
dez_digitos = cpf[:10]
contador_regressivo_2 = 11

resultado = 0
for digito_2 in dez_digitos:
    resultado += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = ((resultado * 10) % 11)   
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'O segundo dígito do CPF número {cpf} é {digito_2}.')










