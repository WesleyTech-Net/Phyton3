ano_2022 = float(input("Insira o total de vendas no ano de 2022: R$ "))
ano_2023 = float(input("Insira o total de vendas no ano de 2023: R$ "))
diferenca = ano_2023 - ano_2022
divisao = diferenca / ano_2022
percentual = divisao * 100

if percentual > 20:
    print(f"A empresa obtive um crescimento de {percentual:.2f}%. BONIFICAÇÃO PARA O TIME DE VENDAS!")
elif  2 < percentual <= 20:
    print(f"A empresa obtive um crescimento de {percentual:.2f}%. PEQUENA BONIFICAÇÃO PARA O TIME DE VENDAS!")
elif -10 < percentual <= 2:
    print(f"A empresa obtive um crescimento de {percentual:.2f}%. PLANEJAMENTO DE POLÍTICAS DE INCENTIVOS À VENDAS!") 
elif percentual <= -10:
    print(f"A empresa obtive um crescimento de {percentual:.2f}%. CORTE DE GASTOS!")    