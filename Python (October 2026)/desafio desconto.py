print('precos das coisas com 5% de desconto')
valor = float(input('defina o valor original do produto: '))

desconto = valor * 0.05

valordesconto = valor - desconto

print('o valor do produto com 5% de desconto é: {:.2f}'.format(valordesconto))