"""
1. Crea una funcion que pida por pantalla un número al usuario y que
controle mediante excepciones lo siguiente:
    a. Solo se podrá introducir numeros enteros
    b. Si el numero es mayor de 10 lanza una excepción con raise la
    cual hayas creado previamente mediante ‘class
    Miexcepcion(Exception):’
"""


class Miexcepcion(Exception):
    number = 0

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"<NumberGreaterThan10Exception> -> {self.number} is greater than 10."


def input_ctrl(msg):
    try:
        n = int(input(msg))
        if n > 10: raise Miexcepcion(n)
    except ValueError:
        print("Invalid input. Integer values only.")
    except Miexcepcion as e:
        print(e)


input_ctrl("Introduce a number: ")

"""
2. Abre un fichero .txt y controla mediante excepciones las diferentes
casuisticas para que el programa no termine de forma inesperada.
Utiliza el finally para cerrar el fichero
"""


f = None
try:
    f = open("file.txt", "r", encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print("Cannot open the specified file.")
except LookupError:
    print("Specified coding error.")
except UnicodeDecodeError:
    print("Decoding error when reading the file.")
except IOError:
    print("Input/output exception.")
finally:
    if f:
        f.close()
