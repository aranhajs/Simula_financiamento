print('Simulação de Financiamento')
print('='*30)
valor_casa = float(input('Digite o Valor do Imovel: '))
salario = float(input('Digite seu Salario: '))
print('='*75)
print('\033[33mExemplo: (60 Meses = 5 anos ) (180 Meses = 15 anos)  (360 Meses = 30 anos)\033[m')
print('='*75)
anos = float(input('Quantidade de Parcelas: '))
juros = (0.70/100 * valor_casa) * anos
valor_parcela = (juros/anos)
parcela_maxima = (salario * 30/100)
print('='*75)
print(f'Preço Final: \033[34mR${juros: .2f}\033[m \nO valor da parcela é: \033[34mR${juros/anos: .2f}\033[m')
print(f'Juros = \033[34mR${juros-valor_casa: .2f}\033[m')
print('='*75)
print(f'')

if valor_parcela >= 30/100 * salario:
    print(f'Renda Insulficiente: \033[31mReprovado\033[m \nSua parcela maxima deve ser: R${parcela_maxima: .2f} ')
else:
    print('Parabens seu fianciamento foi \033[32mAprovado!\033[m')
print('='*75)






