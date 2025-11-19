def programa():
    alumnos = []

    # Pedir número de alumnos con control de errores
    while True:
        try:
            n = int(input("¿Cuántos alumnos? "))
            if n <= 0:
                print("Debe ser un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Introduce un número válido.")

    # Pedir notas
    for i in range(n):
        while True:
            try:
                nota = float(input("Nota: "))
                if nota < 0 or nota > 10:
                    print("La nota debe estar entre 0 y 10.")
                    continue
                alumnos.append(nota)
                break
            except ValueError:
                print("Introduce una nota válida (número).")

    # Calcular media (ya no habrá división por cero)
    media = sum(alumnos) / len(alumnos)
    print("Media:", media)

    # Mostrar aprobados
    print("Aprobados:")
    for nota in alumnos:
        if nota >= 5:
            print(nota)


programa()
