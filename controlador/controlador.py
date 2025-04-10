from modelo.estudiante import Estudiante
from vista.vista import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista()

    def ejecutar(self):
        try:
            cantidad = int(input("Digite el número de estudiantes: "))
            for i in range(cantidad):
                print(f"\n--- Estudiante {i+1} ---")
                nombre = input("Digite el nombre del estudiante: ")
                estudiante = Estudiante(nombre)
                self.vista.pedir_notas(estudiante)
                estudiante.calcular_promedios()
                materias_siguiente = estudiante.materias_disponibles_proximo_semestre()
                self.vista.mostrar_resultados(estudiante, materias_siguiente)
        except ValueError:
            print("ERROR: Digite un número válido.")
