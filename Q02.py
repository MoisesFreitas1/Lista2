print("É ano bissexto ou não é?")
ano = int(input("\nAno: "))
if ((ano % 4) == 0 and ((ano % 400) == 0 or (ano % 100) != 0)):
    print("É ano bissexto.")
else:
    print("Não é ano bissexto.")