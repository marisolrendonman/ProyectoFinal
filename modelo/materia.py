class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 5:
            self.notas.append(nota)

    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0.0
