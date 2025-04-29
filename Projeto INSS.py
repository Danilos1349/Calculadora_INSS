menu_inicial = ''' 
        Calculadora de Desconto INSS

Digite o valor do salário bruto do funcionário:  '''

def calcular_desconto(salario):
    tetos = [0, 1518, 2793.88, 4190.83, 8157.41]
    aliquotas = [0, (7.5 / 100), (9 / 100), (12 / 100), (14 / 100)]
    desconto = 0

    if salario > tetos[len(tetos)-1]:
        return 951.64
    else:
        for i in range(1, len(tetos)):
            if salario > tetos[i]:
                desconto += (tetos[i] - tetos[i-1]) * aliquotas[i]
            else:
                desconto += (salario - tetos[i-1]) * aliquotas[i]
                break
    return desconto

while True:
    salario_funcionario = float(input(menu_inicial))

    if salario_funcionario <= 0:
        print('Valor inválido! Certifique-se de digitar um número maior que 0.')
        continue

    desconto_INSS = calcular_desconto(salario_funcionario)
    salario_liquido = salario_funcionario - desconto_INSS

    print(f'Desconto do INSS: R$ {desconto_INSS:.2f}')
    print(f'Salário líquido: R$ {salario_liquido:.2f}')

    while True:
        novo_calculo = input('Deseja realizar um novo cálculo (Sim ou Não)? ').strip().upper()

        if novo_calculo == 'SIM':
            break  # volta para o começo do loop principal
        elif novo_calculo == 'NÃO' or novo_calculo == 'NAO':
            print('Programa encerrado.')
            exit()
        else:
            print('Opção inválida! Digite "Sim" ou "Não".')
