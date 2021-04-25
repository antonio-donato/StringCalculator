import re


class Stringa:
    def __init__(self):
        self.somma = 0
        self.parametri = ""
        self.default_delimiter = ","

    def add(self, parametri):
        lista_parametri = []
        self.parametri = parametri

        if self.parametri != " ":
            if self.parametri.startswith("\\"):
                self.default_delimiter = self.parametri[1]
                self.parametri = parametri[3:]

            if self.parametri.endswith("\n"):
                return 0

            self.default_delimiter = self.default_delimiter + "|\n"
            lista_parametri = re.split(rf"{self.default_delimiter}", self.parametri)

        for elemento in lista_parametri:
            self.somma += int(elemento)

        return self.somma
