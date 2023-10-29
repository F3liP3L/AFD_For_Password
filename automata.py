import re

lowercase = r"^[a-z]+$"
uppercase = r"^[A-Z]+$"
number = r"^\d+$"
specialCharacter = r"^[!¡@#\$%^&\*\(\)_\+\{\}\[\]:;<>,\.\¿\?~\\/\=]+$"


def validExpression(expression, symbol):
    isValid = False
    if re.match(expression, symbol):
        isValid = True
    return isValid


class Automata:
    def __init__(self):
        self.currentStatus = 0

    def transition(self, chain):
        for symbol in chain:
            if self.currentStatus == 0 and validExpression(specialCharacter, symbol):
                self.currentStatus = 1
            elif self.currentStatus == 0 and validExpression(uppercase, symbol):
                self.currentStatus = 2
            elif self.currentStatus == 0 and validExpression(lowercase, symbol):
                self.currentStatus = 3
            elif self.currentStatus == 0 and validExpression(number, symbol):
                self.currentStatus = 4
            else:
                self.currentStatus = -1  # Estado de error

    def accepted(self):
        return self.currentStatus == 4


def main():
    automata = Automata()
    password = input("Ingresa una contaseña segura :D: ")

    automata.transition(password)

    if automata.accepted():
        print("La cadena es aceptada.")
    else:
        print("La cadena no es aceptada.")


if __name__ == "__main__":
    main()
