socios = {
    "Ana": 25,
    "Luis": 30,
    "María": 28
}

while True:
    print("\n===== GIMNASIO =====")
    print("1. Ver socios")
    print("2. Agregar socio")
    print("3. Modificar cuota")
    print("4. Eliminar socio")
    print("5. Promedio de cuotas")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- SOCIOS ---")
        for nombre, cuota in socios.items():
            print(f"{nombre}: ${cuota}")

    elif opcion == "2":
        nombre = input("Nombre: ")
        cuota = float(input("Cuota: "))
        socios[nombre] = cuota
        print("✅ Socio agregado.")

    elif opcion == "3":
        nombre = input("Nombre a modificar: ")
        if nombre in socios:
            socios[nombre] = float(input("Nueva cuota: "))
            print("✅ Cuota actualizada.")
        else:
            print("❌ Socio no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if nombre in socios:
            del socios[nombre]
            print("✅ Socio eliminado.")
        else:
            print("❌ Socio no encontrado.")

    elif opcion == "5":
        if socios:
            promedio = sum(socios.values()) / len(socios)
            print(f"\nPromedio de cuotas: ${promedio:.2f}")
            print("--- Cuotas altas y bajas ---")
            for nombre, cuota in socios.items():
                if cuota > promedio:
                    print(f"{nombre} paga más del promedio (${cuota})")
                else:
                    print(f"{nombre} paga menos del promedio (${cuota})")
        else:
            print("No hay socios registrados.")

    elif opcion == "6":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")
