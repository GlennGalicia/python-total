from os import system


class Persona:

    # Atributos de instancia
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    # Atributos de instancia
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Metodo sobre escrito
    def __str__(self):
        return f'{self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}'

    # Metodo de instancia propio
    def depositar_dinero(self, deposito):
        self.balance += round(deposito)

    # Metodo de instancia propio
    def retirar_dinero(self, retiro):
        if retiro <= self.balance:
            self.balance -= retiro
            return True
        else:
            return False


def crear_cliente():
    print('Bienvenido al Banco del Bienestar')
    nombre = input('Ingresa tu Nombre: ').capitalize()
    apellido = input('Ingresa tu Apellido: ').capitalize()
    num_cuenta = int(input('Ingresa tu No. Cuenta: '))
    return Cliente(nombre, apellido, num_cuenta)


def inicio():
    en_banco = True
    mi_cliente = crear_cliente()
    system('clear')
    print(mi_cliente)

    while en_banco:
        print('\nQue actividad realizas hoy:\n'
              '[1]- Realizar Deposito.\n'
              '[2]- Realizar Retiro.\n'
              '[3]- Salir.')
        select = int(input('Elige una opción: '))

        if select == 1:
            # Depositar dinero
            system('clear')
            deposito = float(input('Ingresa el Monto a depositar: $'))
            mi_cliente.depositar_dinero(deposito)
            system('clear')
            print(f'Depositado exitosamente...')
        elif select == 2:
            # Retirar dinero
            system('clear')
            retiro = round(float(input('Ingresa el Monto a retirar: $')))
            dinero_retirado = mi_cliente.retirar_dinero(retiro)
            system('clear')
            if dinero_retirado:
                print(f'Haz retirado ${retiro} exitosamente...')
            else:
                print(f'El monto ${retiro} es mayor a tu saldo actual...\n')
        elif select == 3:
            en_banco = False
            continue
        else:
            system('clear')
            print('Ingresa una opción valida !!!')
            pass
        print(mi_cliente)

inicio()
