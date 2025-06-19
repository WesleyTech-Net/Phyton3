def div():
    try:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        res = n1 / n2
    except ZeroDivisionError:
        print("Oops! Erro de divisão por zero...")
    except ValueError:
        print("Oops! Número inválido. Tente novamente...")
    except:
        print("Algo de errado aconteceu...")
    else:
        return res
    finally:
        print("Executará sempre!")

#PROMAGRA PRINCIPAL
print(div())