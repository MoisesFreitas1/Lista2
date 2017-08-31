import math

print("É triângulo ou não é?")
print("        /\          ")
print("       /  \          ")
print("    B /    \ C         ")
print("     /      \          ")
print("    /________\          ")
print("        A          ")
a = float(input("\nLado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
if (((math.fabs(b-c)<a) and (a<(b+c))) and ((math.fabs(a-c)<b) and (b<(a+c)))) and ((math.fabs(a-b)<c) and (c<(a+b))):
    if ((a == b) and (a == c)):
        print("   É um triângulo equilátero.")
    elif ((a != b) and (b != c) and (a != c)):
        print("   É um triângulo escaleno.")
    elif (((a == b) and (b != c)) or ((a == c) and (c != b)) or ((b == c) and (c != a))):
        print("   É um triângulo isósceles.")
else:
    print("   Não é um triângulo.")