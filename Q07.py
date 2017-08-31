print("Custo com tinta")
tam = float(input("Tamanho da parede (m2): "))
litros = tam/3
latas = litros/18
resto = litros%18
dizima = resto/18
latas = latas - dizima
if dizima>0:
    latas = latas + 1
custo = latas * 80
print(" - Número de latas: %d"%latas)
print(" - Custo: R$ %.2f"%custo)