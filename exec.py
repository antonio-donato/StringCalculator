import re


class Stringa:
    def __init__(self):
        self.somma = 0
        self.parametri = ""

    def add(self, parametri):
        lista_parametri = []
        self.parametri = parametri

        if self.parametri != " ":
            if self.parametri.endswith("\n"):
                return 0
            lista_parametri = re.split(r",|\n", self.parametri)

        for elemento in lista_parametri:
            self.somma += int(elemento)

        return self.somma
