class CuentaBancaria:
    def __init__(self, balance=1000):
        self.balance = balance

    def depositar(self, deposito):
        if deposito > 0:
            self.balance += deposito
            print(f"\nDepósito realizado con éxito, su saldo ahorita es de: ${self.balance}")
        else:
            print("\nEl depósito debe ser mayor a 0.")

    def retirar(self, retiro):
        if retiro > 0:
            if retiro <= self.balance:
                self.balance -= retiro
                print(f"\nRetiro exitoso. Su saldo actual es: ${self.balance}")
            else:
                print("\nNo tienes plata pobre")
        else:
            print("\nEl retiro debe ser mayor a 0.")

    def ver_saldo(self):
        print(f"\nSu saldo actual es: ${self.balance}")

class MenuBancario:
    def __init__(self):
        self.cuenta = CuentaBancaria()

    def mostrar_menu(self):
        while True:
            print()
            print("=== Menú Bancario By Steve ===")
            print()
            print("Depositar    = 1")
            print("Retirar      = 2")
            print("Ver saldo    = 3")
            print("Salir        = 4")
            print()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                deposito = input("Ingrese dinero a depositar: ")
                if deposito.replace(".", "", 1).isdigit():
                    self.cuenta.depositar(float(deposito))
                else:
                    print("Entrada inválida. Debe ingresar un número.")

            elif opcion == "2":
                retiro = input("Ingrese el monto a retirar: ")
                if retiro.replace(".", "", 1).isdigit():
                    self.cuenta.retirar(float(retiro))
                else:
                    print("Entrada inválida. Debe ingresar un número.")

            elif opcion == "3":
                self.cuenta.ver_saldo()

            elif opcion == "4":
                print("\nGracias por usar el sistema bancario de Steve. ¡Bye!")
                break

            else:
                print("\nOpción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu = MenuBancario()
    menu.mostrar_menu()
