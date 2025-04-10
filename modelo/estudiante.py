class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = [
            Materia("Inglés I"),
            Materia("Francés II"),
            Materia("Corrección de estilo"),
            Materia("Italiano I")
        ]

    def calcular_promedios(self):
        self.promedios = {materia.nombre: materia.promedio() for materia in self.materias}

    def materias_disponibles_proximo_semestre(self):
        disponibles = []

        nombres_materias = {m.nombre: m for m in self.materias}

        if all(m.promedio() >= 3 for m in self.materias):
            return [
                "Inglés II",
                "Francés III",
                "Lingüística textual",
                "Italiano II"
            ]

        if nombres_materias["Inglés I"].promedio() >= 3:
            disponibles.append("Inglés II")
        if nombres_materias["Francés II"].promedio() >= 3:
            disponibles.append("Francés III")
        if nombres_materias["Corrección de estilo"].promedio() >= 3:
            disponibles.append("Lingüística textual")
        if nombres_materias["Italiano I"].promedio() >= 3:
            disponibles.append("Italiano II")

        return disponibles

    def materias_que_debe_repetir(self):
        return [materia.nombre for materia in self.materias if materia.promedio() < 3]
