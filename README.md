# python3_Validador_cpf
#Cálculo do primeiro dígito do CPF
CPF: 014.446.956-14
Colete a soma dos 9 primeiros dígitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex: 

10  9  8  7  6  5  4  3  2
 0  1  4  4  4  6  9  5  6
 0  9  32 28 24 30 36 15 12 

Somar todos os resultados:
0+9+32+28+24+30+36+15+12 =  186

Multiplicar o resultado anterior por 10
186 * 10 = 1860

Obter o resto da divisão da conta anterior por 11
1860 / 11 = 1

Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso
    resultado é o valor da conta

O primeiro dígito do CPF é 1   

-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Cálculo do segundo dígito do CPF
CPF: 014.446.956-14
Colete a soma dos 9 primeiros dígitos do CPF, 
MAIS O PRIMEIRO DÍGITO
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex: 

11  10  9  8  7  6  5  4  3  2
 0   1  4  4  4  6  9  5  6  1
 0  10 36 32 28 36 45 20 18  2

Somar todos os resultados:
0+10+36+32+28+36+45+20+18+2 = 227

Multiplicar o resultado anterior por 10
227 * 10 = 2270

Obter o resto da divisão da conta anterior por 11
2270 / 11 = 4

Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso
    resultado é o valor da conta

O segundo dígito do CPF é 4

