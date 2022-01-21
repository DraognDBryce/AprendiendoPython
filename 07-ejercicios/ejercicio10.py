"""
El programa tiene que pedir la nota de 15 alumnos y mostrar por pantalla cuantos han aprobado y cuantos suspendido
"""
suspenso = 0
aprobado = 0
numeroAlumnos = int(input("¿Cuantos alumnos tienes?: "))
for notas in range (numeroAlumnos):
    notaAlumno = int(input("Indique la nota del alumno: "))

    if notaAlumno < 5:
        print(f"Alumno {notas} SUSPENSO")
        suspenso += 1
    else:
        print(f"Alumno {notas} APROBADO")
        aprobado += 1

print(f"Alumnos SUSPENSOS {suspenso}")
print(f"Alumnos APROBADOS {aprobado}")


notas = 1
suspenso = 0
aprobado = 0

numeroAlumnos = int(input("¿Cuantos alumnos tienes?: "))

while notas <= numeroAlumnos:
    pregunta = int(input("Indique la nota del alumno: "))
    if pregunta < 5:
        print(f"El alumno {notas} a SUSPENDIDO")
        suspenso += 1
    else:
        print(f"El alumno {notas} a APROBADO")
        aprobado += 1
    notas += 1
print(f"Alumnos SUSPENSOS {suspenso}")
print(f"Alumnos APROBADOS {aprobado}")
