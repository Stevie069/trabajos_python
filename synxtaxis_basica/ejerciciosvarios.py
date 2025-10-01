#   EJERCICIOS VARIOS :)

# #Validación de usuario
# user='admin'
# passw='123'

# useri=input("Ingrese usuario: ")
# passwi=input("Ingrese contraseña: ")


# if useri==user and passwi==passw:
#     print("usuario admin bienvenido")
# else:
#     print("Contraseña o usuario incorrecto")

# #Definir si un número es par o impar

# while True:
#     n=int(input("Ingrese un número: "))

#     if n % 2==0:
#         print(f'El número {n} es par')
#     else:
#         print(f'El número {n} es impar')   


#contar números de una lista


# lista=[]
# suma=1

# for i in range(10):
#     numero=int(input("Ingrese número: "))
#     suma=suma+numero
#     lista.append(numero)

# print(f'La suma es: ', {suma})
# print(f'De la lista: ', {list})



#Ejercicios bbancario, usuario puede hacer deposito, sacar dinero y ver su saldo actual


# print()
# print("Menu Bancario")
# print()
# print("Deposito: 1")
# print("Retiro:   2")
# print("Saldo:    3")

# balance=1000
# saldo=0
# print()
# n=int(input("Selecione: "))
# if n==1:
#     depo=int(input("Ingrese valor a depositar: "))
#     balance=balance+depo
#     print(f'Gracias por su depósito, su saldo actual es de', saldo)
# elif n==2:
#     depo=int(input("Ingrese valor a depositar: "))
#     balance=balance+depo
#     print(f'Gracias por su depósito, su saldo actual es de', saldo)


# Ejercicio bancario: el usuario puede depositar, retirar y ver su saldo actual

# balance=1000 

# while True:
#     print()
#     print("=== Menú Bancario ===")
#     print()
#     print("Depositar    = 1")
#     print("Retirar      = 2")
#     print("Ver saldo    = 3")
#     print("Salir        = 4")
#     print()
#     opcion = input("Seleccione una opción: ")

#     if opcion == "1":
#         deposito = float(input("Ingrese dinero a depositar: "))
#         if deposito > 0:
#             balance += deposito
#             print()
#             print(f"Deposito realizado con éxito, su saldo ahorita es de: ${balance}")

#     elif opcion == "2":
#         retiro = float(input("Ingrese el monto a retirar: "))
#         if retiro > 0:
#             if retiro <= balance:
#                 balance -= retiro
#                 print(f"Retiro exitoso. Su saldo actual es: ${balance}")
#             else:
#                 print("No tienes plata pobre")
#     elif opcion == "3":
#         print(f"Su saldo actual es: ${balance}")

#     elif opcion == "4":
#         print("Gracias por usar el sistema bancario. ¡Bye!")
#         break


#CLASES!!!

# class Estudiante:
#     def __init__(self,nombre, curso='IA'):
#         print('El estudiante a sido registrado')
#         self.nombre=nombre
#         self.curso=curso
#     def datosDelEstudiante(self):
#         print(f'Nombre: {self.nombre} curso: {self.curso}')
#         return

# Estudiante1=Estudiante('Steve')
# Estudiante2=Estudiante('Aby', 'Gasronomía')


# Estudiante1.datosDelEstudiante()
# Estudiante2.datosDelEstudiante()



class Estudiante:
    def __init__(self,nombre, curso='IA'):
        print('El estudiante a sido registrado')
        self.nombre=nombre
        self.curso=curso
        
    def datosDelEstudiante(self,estado='Inactivo'):
        self.estado=estado
        print(f'Nombre: {self.nombre} curso: {self.curso} estado:{self.estado}')
        return

Estudiante1=Estudiante('Steve')
Estudiante2=Estudiante('Aby', 'Gasronomía')


Estudiante1.datosDelEstudiante()
Estudiante2.datosDelEstudiante()