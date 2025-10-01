class CuentaBancaria:
    def __init__(self, balance_inicial=1000):
        self.balance = balance_inicial

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"\nDepósito realizado. Tu saldo actual es de: ${self.balance}")
        else:
            print("\nEl monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto <= 0:
            print("\nEl monto a retirar debe ser mayor a 0 loco.")
        elif monto > self.balance:
            print("\nDinero insuficiente. No se realizo la operación.")
        else:
            self.balance -= monto
            print(f"\nRetiro exitoso. Tu saldo actual es de: ${self.balance}")

    def ver_saldo(self):
        print(f"\nSu saldo actual es: ${self.balance}")


class MenuBancario:
    def __init__(self):
        self.cuenta = CuentaBancaria()

    def mostrar_menu(self):
        while True:
            print("\n=== Menú Bancario ===")
            print("Depositar        = 1")
            print("Retirar          = 1")
            print("Ver saldo        = 1")
            print("Salir            = 1")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    monto = float(input("Ingrese dinero a depositar: "))
                    self.cuenta.depositar(monto)
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número.")

            elif opcion == "2":
                try:
                    monto = float(input("Ingrese el monto a retirar: "))
                    self.cuenta.retirar(monto)
                except ValueError:
                    print("Entrada inválida. Debe ingresar un número.")

            elif opcion == "3":
                self.cuenta.ver_saldo()

            elif opcion == "4":
                print("Gracias por usar el sistema bancario. ¡Adiós!")
                break

            else:
                print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu = MenuBancario()
    menu.mostrar_menu()
