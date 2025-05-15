nome = input("Digite aqui seu nome:")
salario_fixo = float(input("Digite aqui seu salario:"))
total_em_vendas = float(input("Digite o total em vendas:"))

comissao = total_em_vendas * 0.15

total_a_receber = salario_fixo + comissao

print(f'O total é {total_a_receber:.2f}')