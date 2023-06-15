#Início - Entrada de dados
while True:
    while True:
        print("Opção 1 - Utilizar de dois número específicos.")
        print("Opção 2 - Usar apenas um número em uma tabuada do 1 ao 10.")
        es = str(input("Digite o número da opção desejada: "))
        if es in ["1", "2"]:
            break
        print("Não foi possível entender o seu comando. Por favor, digite apenas 1 ou 2! Tente novamente.")

#Entrada de dados avançado
    if es == "1":
        while True:
            try:
                n2 = int(input("Digite o primeiro numéro: "))
                break
            except ValueError:
                print("Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.")
        while True:
            try:
                n3 = int(input("Digite o segundo número: "))
                break
            except ValueError:
                print("Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.")

        if n2 == 1 and n3 == 8:
            print()
            print("Eu te amo Lorena <3")
            print()
            acontinue = input("Pressione ENTER para continuar.")
        while True:
            print("Opção 1 - Somar")
            print("Opção 2 - Subtrair")
            print("Opção 3 - Multiplicar")
            print("Opção 4 - Dividir")
            c = str(input("Digite o número da opção desejada: "))
            if c in ["1", "2", "3", "4"]:
                break
            print("Não foi possível entender o seu comando. Por favor, digite uma das 4 opções! Tente novamente.")
    elif es == "2":
        while True:
            try:
                n1 = int(input("Digite um número qualquer para a tabuada de 1 a 10: "))
                break
            except ValueError:
                print("Não foi possível entender o seu comando. Por favor, digite apenas números! Tente novamente.")
        while True:
            es2 = str(input("Deseja 4 tabuadas? Subtrair, somar, dividir e multiplicar? \nS para Sim \nN para Não \nDigite: "))
            if es2 == "s" or es2 == "S" or es2 == "n" or es2 == "N":
                break
            print("Não foi possível entender o seu comando. Por favor, digite apenas \"S\" ou \"N\"! Tente novamente.")
        if es2 == "n" or es2 == "N":
            while True:
                print("Opção 1 - Somar")
                print("Opção 2 - Subtrair")
                print("Opção 3 - Multiplicar")
                print("Opção 4 - Dividir")
                c = str(input("Digite o número da opção desejada: "))
                if c == "1" or c == "2" or c == "3" or c == "4":
                    break
                print("Não foi possível entender o seu comando. Por favor, escolha uma das 4 opções! Tente novamente.")

#Processamento de dados 01
    if es2 == "s" or es2 == "S":
        print()
        print("SOMA")
        print(n1, "+ 1 = {:2}".format(n1+1), "|", n1, "+ 2 = {:2}".format(n1+2))
        print(n1, "+ 3 = {:2}".format(n1+3), "|", n1, "+ 4 = {:2}".format(n1+4))
        print(n1, "+ 5 = {:2}".format(n1+5), "|", n1, "+ 6 = {:2}".format(n1+6))
        print(n1, "+ 7 = {:2}".format(n1+7), "|", n1, "+ 8 = {:2}".format(n1+8))
        print(n1, "+ 9 = {:2}".format(n1+9), "|", n1, "+ 10 = {:2}".format(n1+10))
        print()
        print("SUBTRAÇÃO")    
        print(n1, "- 1 = {:2}".format(n1-1), "|", n1, "- 2 = {:2}".format(n1-2))
        print(n1, "- 3 = {:2}".format(n1-3), "|", n1, "- 4 = {:2}".format(n1-4))
        print(n1, "- 5 = {:2}".format(n1-5), "|", n1, "- 6 = {:2}".format(n1-6))
        print(n1, "- 7 = {:2}".format(n1-7), "|", n1, "- 8 = {:2}".format(n1-8))
        print(n1, "- 9 = {:2}".format(n1-9), "|", n1, "- 10 = {:2}".format(n1-10))
        print()
        print("MULTIPLICAÇÃO")
        print(n1, "x 1 = {:2}".format(n1*1), "|", n1, "x 2 = {:2}".format(n1*2))
        print(n1, "x 3 = {:2}".format(n1*3), "|", n1, "x 4 = {:2}".format(n1*4))
        print(n1, "x 5 = {:2}".format(n1*5), "|", n1, "x 6 = {:2}".format(n1*6))
        print(n1, "x 7 = {:2}".format(n1*7), "|", n1, "x 8 = {:2}".format(n1*8))
        print(n1, "x 9 = {:2}".format(n1*9), "|", n1, "x 10 = {:2}".format(n1*10))
        print()
        print("DIVISÃO")
        print(n1, "/ 1 = {:2}".format(n1/1), "|", n1, "/ 2 = {:2}".format(n1/2))
        print(n1, "/ 3 = {:2}".format(n1/3), "|", n1, "/ 4 = {:2}".format(n1/4))
        print(n1, "/ 5 = {:2}".format(n1/5), "|", n1, "/ 6 = {:2}".format(n1/6))
        print(n1, "/ 7 = {:2}".format(n1/7), "|", n1, "/ 8 = {:2}".format(n1/8))
        print(n1, "/ 9 = {:2}".format(n1/9), "|", n1, "/ 10 = {:2}".format(n1/10))
        print()

#Processamento de dados 02
    else:
        if es == "2" and c == "1":
            print()
            print(n1, "+ 1 = {:2}".format(n1+1), "|", n1, "+ 2 = {:2}".format(n1+2))
            print(n1, "+ 3 = {:2}".format(n1+3), "|", n1, "+ 4 = {:2}".format(n1+4))
            print(n1, "+ 5 = {:2}".format(n1+5), "|", n1, "+ 6 = {:2}".format(n1+6))
            print(n1, "+ 7 = {:2}".format(n1+7), "|", n1, "+ 8 = {:2}".format(n1+8))
            print(n1, "+ 9 = {:2}".format(n1+9), "|", n1, "+ 10 = {:2}".format(n1+10))
            print()
        elif es == "2" and c == "2":
            print()
            print(n1, "- 1 = {:2}".format(n1-1), "|", n1, "- 2 = {:2}".format(n1-2))
            print(n1, "- 3 = {:2}".format(n1-3), "|", n1, "- 4 = {:2}".format(n1-4))
            print(n1, "- 5 = {:2}".format(n1-5), "|", n1, "- 6 = {:2}".format(n1-6))
            print(n1, "- 7 = {:2}".format(n1-7), "|", n1, "- 8 = {:2}".format(n1-8))
            print(n1, "- 9 = {:2}".format(n1-9), "|", n1, "- 10 = {:2}".format(n1-10))
            print()
        elif es == "2" and c == "3":
            print()
            print(n1, "x 1 = {:2}".format(n1*1), "|", n1, "x 2 = {:2}".format(n1*2))
            print(n1, "x 3 = {:2}".format(n1*3), "|", n1, "x 4 = {:2}".format(n1*4))
            print(n1, "x 5 = {:2}".format(n1*5), "|", n1, "x 6 = {:2}".format(n1*6))
            print(n1, "x 7 = {:2}".format(n1*7), "|", n1, "x 8 = {:2}".format(n1*8))
            print(n1, "x 9 = {:2}".format(n1*9), "|", n1, "x 10 = {:2}".format(n1*10))
            print()
        elif es == "2" and c == "4":
            print()
            print(n1, "/ 1 = {:2}".format(n1/1), "|", n1, "/ 2 = {:2}".format(n1/2))
            print(n1, "/ 3 = {:2}".format(n1/3), "|", n1, "/ 4 = {:2}".format(n1/4))
            print(n1, "/ 5 = {:2}".format(n1/5), "|", n1, "/ 6 = {:2}".format(n1/6))
            print(n1, "/ 7 = {:2}".format(n1/7), "|", n1, "/ 8 = {:2}".format(n1/8))
            print(n1, "/ 9 = {:2}".format(n1/9), "|", n1, "/ 10 = {:2}".format(n1/10))
            print()

#Processamento de dados 03
        else:
            if es == "1" and c == "1":
                print()
                print(n2, "+", n3, "= {:2}".format(n2+n3))
                print()
            elif c == "2" and es == "1":
                print()
                print(n2, "-", n3, "= {:2}".format(n2-n3))
                print()
            elif c == "3" and es == "1":
                print()
                print(n2, "x", n3, "= {:2}".format(n2*n3))
                print()
            else:
                print()
                print(n2, "/", n3, "= {:2}".format(n2/n3))
                print()

#Repetição opcional
    fim = input("Deseja voltar do começo? \nS para Sim\nN para Não\nDigite: ")
    print()
    if fim == "n" or fim == "N":
        print("Obrigado por testar o script ;)")
        bfim = input("Pressione ENTER para continuar.")
        break