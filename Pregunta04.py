# Función para obtener el número de estudiantes
def obtener_numero_estudiantes():
    num_estudiantes = int(input("Ingresa el número de estudiantes: "))
    return num_estudiantes

# Función para obtener la información de un estudiante
def obtener_informacion_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"Ingresa la calificación {i+1}: "))
        calificaciones.append(calificacion)
    return {
        "nombre": nombre,
        "calificaciones": calificaciones
    }

# Función para imprimir la información de un estudiante
def imprimir_informacion_estudiante(estudiante):
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Calificaciones: {estudiante['calificaciones']}")
    print()

# Obtén el número de estudiantes
num_estudiantes = obtener_numero_estudiantes()

# Inicializa una lista para almacenar la información de todos los estudiantes
estudiantes = []

# Obtiene la información de cada estudiante
for i in range(num_estudiantes):
    estudiante = obtener_informacion_estudiante()
    estudiantes.append(estudiante)

# Imprime la información de todos los estudiantes
print("Información de los estudiantes:")
for estudiante in estudiantes:
    imprimir_informacion_estudiante(estudiante)
