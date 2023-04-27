# 1-Faça um programa que peça dois números inteiros e imprima a soma desses números
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

valor = num1 + num2

print('A soma dos números é', valor)

# 2-Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
valor = float(input('Informe o valor (em metros): '))

result = valor * 1000

print('O valor (em milímetros) é de', result)

# 3- Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input('Informe a quantidade de dias: '))
horas = int(input('Informe a quantidade de horas: '))
minutos = int(input('Informe a quantidade de minutos: '))
segundos = int(input('Informe a quantidade de segundos: '))

total_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos

print(f"{dias} dias é igual a {dias * 24 * 60 * 60} segundos")
print(f"{horas} horas é igual a {horas * 60 * 60} segundos")
print(f"{minutos} minutos é igual a {minutos * 60} segundos")
print(f"{segundos} segundos é igual a {segundos} segundos")

# 4- Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
valor = float(input('Informe o valor do salário: '))
porcentagem = float(input('Informe a porcentagem de aumento: '))

valor_aumento = valor * porcentagem / 100
result = valor + valor_aumento

print('O valor do aumento é de', valor_aumento, 'R$')
print('O valor do aumento é de', valor_aumento,
      'R$, e o salário passará para', result, 'R$')

# 5-Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input("Digite o preço da mercadoria: "))
desconto_percentual = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco * (desconto_percentual / 100)
preco_final = preco - valor_desconto

print(f"O desconto será de R${valor_desconto:.2f}")
print(f"O preço final a pagar será de R$ {preco_final:.2f}")

# 6-Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade_media = float(
    input("Digite a velocidade média esperada (em km/h): "))

tempo_horas = distancia / velocidade_media

tempo_minutos = tempo_horas * 60

if tempo_minutos > 60:
    print("O tempo de viagem do carro será de {:.2f} horas.".format(
        tempo_horas))
else:
    print("O tempo de viagem do carro será de {:.0f} minutos.".format(
        tempo_minutos))

# 7-Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32 . Faça agora o contrário, de Fahrenheit para Celsius.
temperatura = int(input('Informe a temperatura (em fahrenheit): '))

conversao = (temperatura - 32) / 1.8

print(
    f'A tempereatura de {temperatura:.0f} fahrenheit será de {conversao:.0f} celsius.')

# 8-Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_locacao = int(input("Digite a quantidade de dias de locação: "))

preco_dias = dias_locacao * 60
preco_km = km_percorridos * 0.15
preco_total = preco_dias + preco_km

print("O preço a pagar pelo aluguel do carro é de R$ {:.2f}".format(
    preco_total))

# 9-Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_por_dia = int(
    input("Digite a quantidade de cigarros fumados por dia: "))
anos_de_fumo = int(input("Digite a quantidade de anos de fumo: "))

cigarros_fumados = cigarros_por_dia * 365 * anos_de_fumo
tempo_perdido = cigarros_fumados * 10 / 1440

print("O fumante perderá {:.2f} dias de vida.".format(tempo_perdido))

# 10-Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
num = 2 ** 1000000
num_str = str(num)
num_digits = len(num_str)
print("O número 2 elevado a um milhão tem", num_digits, "dígitos.")
