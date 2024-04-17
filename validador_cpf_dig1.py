cpf = '01444695614'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado = 0
for digito_1 in nove_digitos:
    resultado += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = ((resultado * 10) % 11)   
digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'O primeiro dígito do CPF número {cpf} é {digito_1}.')









