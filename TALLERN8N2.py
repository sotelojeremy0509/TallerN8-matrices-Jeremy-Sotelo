
curso_A = {
    "Ana", "Carlos", "Laura", "Pedro",
    "Sofia", "Andres", "Camila"
}

curso_B = {
    "Laura", "Pedro", "Daniel", "Sofia",
    "Mateo", "Valentina"
}


def analizar_cursos():

    print("\n========== PARTICIPANTES ==========")

    print("Curso A:", curso_A)
    print("Curso B:", curso_B)

    
    todos = curso_A | curso_B

    print("\nCantidad de estudiantes diferentes:", len(todos))

   
    ambos = curso_A & curso_B

    print("\nEstudiantes inscritos en ambos cursos:")
    print(ambos)

   
    solo_A = curso_A - curso_B

    print("\nEstudiantes únicamente del curso A:")
    print(solo_A)

   
    solo_B = curso_B - curso_A

    print("\nEstudiantes únicamente del curso B:")
    print(solo_B)

   
    exactamente_uno = curso_A ^ curso_B

    print("\nEstudiantes inscritos exactamente en un curso:")
    print(exactamente_uno)

   
    if curso_A.issubset(curso_B):
        print("\nTodos los estudiantes del curso A están en el curso B.")
    else:
        print("\nNo todos los estudiantes del curso A están en el curso B.")



analizar_cursos()

print("\n========== AGREGAR ESTUDIANTE ==========")

nombre = input("Ingrese el nombre del estudiante: ")
curso = input("¿A qué curso desea agregarlo? (A/B): ").upper()

if curso == "A":
    curso_A.add(nombre)
    print("Estudiante agregado al curso A.")

elif curso == "B":
    curso_B.add(nombre)
    print("Estudiante agregado al curso B.")

else:
    print("Curso no válido.")


if curso in ["A", "B"]:
    print("\n========== RESULTADOS ACTUALIZADOS ==========")
    analizar_cursos()
