class Vista:
    def pedir_notas(self, estudiante):
        for materia in estudiante.materias:
            print(f"Ingrese 5 notas para {materia.nombre}:")
            notas = []
            for i in range(5):
                while True:
                    try:
                        nota = float(input(f"Nota {i+1}: "))
                        if 0 <= nota <= 5:
                            notas.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 5.")
                    except ValueError:
                        print("Ingrese un número válido.")
            materia.notas = notas

    def mostrar_resultados(self, estudiante, materias_siguiente):
        print(f"\n--- Calificación final de {estudiante.nombre} en el semestre ---")
        for nombre, promedio in estudiante.promedios.items():
            estado = "Aprobado" if promedio >= 3 else "Reprobado"
            print(f"{nombre}: Promedio = {promedio:.2f} -> {estado}")

        print("\nMaterias que podrá cursar el siguiente semestre:")
        for m in materias_siguiente:
            print(f"- {m}")

        materias_repetir = estudiante.materias_que_debe_repetir()
        if materias_repetir:
            print("\nMaterias que deberá repetir el próximo semestre:")
            for m in materias_repetir:
                print(f"- {m}")
        else:
            print("\n¡Felicidades! No debe repetir ninguna materia.")
