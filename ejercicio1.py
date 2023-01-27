import calculadora.operaciones as ope
def main():
    
    num1: float = 0
    num2: float = 0
    operacion: str = None

    while "salir" != operacion:

        num1 = float (input("Escribe un numero: "))
        num2 = float (input("Escribe otro numero: "))
        operacion = input("escriba la operacion que desea realizar (Suma, Resta, Multiplicacion o Division): ")

        match operacion:
            case "suma":
                print(f"Suma de los {num1} + {num2} = {ope.suma(num1, num2)}")
            case "resta":
                print(f"Resta de los {num1} - {num2} = {ope.resta(num1, num2)}")
            case "multiplicacion":
                print(f"Multiplicación de los {num1} * {num2} = {ope.multiplicacion(num1, num2)}")
            case "division":
                print(f"Division de los {num1} / {num2} = {ope.division(num1, num2)}")


        operacion = input("Para realizar otra operacion pulse enter y para salir escribe 'salir'").lower()

    print("------------------------------------------")

if __name__ == '__main__':
    main()
