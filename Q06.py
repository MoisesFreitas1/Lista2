print("Cálculo do salário líquido")
hora = float(input("Valor da hora de trabalho: R$"))
nhoras = int(input("Horas trabalhadas: "))
salariobruto = nhoras*hora
ir = salariobruto*0.11
inss = salariobruto*0.08
sindicato = salariobruto*0.05
salarioliquido = salariobruto - ir - inss - sindicato
print("+Salário Bruto: R$%.2f"%salariobruto)
print("-IR: R$%.2f"%ir)
print("-INSS: R$%.2f"%inss)
print("-Sindicato: R$%.2f"%sindicato)
print("=Salário Líquido: R$%.2f"%salarioliquido)