print("Cálculo de multa por execesso de peixes\n")
peso = float(input("Peso (kg): "))
if (peso-50) > 0:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print("\nExcesso: %.1f kg"%excesso)
print("Multa: R$ %.2f"%multa)