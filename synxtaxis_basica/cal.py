#Basic Calculator by: Steve


print()
Ini=int(input("¿Desea iniciar calculardora básica? Si = 1, Cerrar = 0: "))
while Ini==1:
    N1=float(input("Ingrese primer número: "))
    Op=input("Ingrese operación + - * /: ")
    N2=float(input("Ingrese seungo número: "))
    print()
    if Op=='+':
        OpF= N1 + N2
        print(N1, " + ", N2," = ", OpF)
        print()
    elif Op=='-':
        OpF= N1 - N2
        print(N1, " - ", N2," = ", OpF)
        print()
    elif Op=='*':
        OpF= N1 * N2
        print(N1, " x ", N2," = ", OpF)
        print()
    elif Op=='/':
        OpF= N1 / N2
        print(N1, " / ", N2," = ", OpF)
        print()
    Ini=int(input("¿Desea repetir calculadora? Si = 1, Cerrar = 0: "))
print()
print("Gracias por usar calculadora básica by Steve")