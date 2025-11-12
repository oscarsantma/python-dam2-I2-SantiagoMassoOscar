# Lista donde guardamos los productos de la frutería
frutas = []

# Añadir fruta nueva
def agregar_fruta(frutas, nombre, precio, cantidad):
    if not nombre:
        print("Error: el nombre está vacío.")
        return
    
    if type(precio) not in (int, float) or type(cantidad) not in (int, float):
        print("Error: precio o cantidad no son números.")
        return

    # Evitar duplicados
    for f in frutas:
        if f["nombre"].lower() == nombre.lower():
            print("Error: esa fruta ya existe.")
            return

    nueva = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    frutas.append(nueva)
    print("✅ Fruta añadida correctamente.\n")


# Buscar fruta por nombre
def buscar_fruta(frutas, nombre):
    for f in frutas:
        if f["nombre"].lower() == nombre.lower():
            return f
    return None


# Calcular precio medio
def precio_medio(frutas):
    if len(frutas) == 0:
        return None
    total = 0
    for f in frutas:
        total += f["precio"]
    return total / len(frutas)


# Calcular precio máximo
def precio_maximo(frutas):
    if len(frutas) == 0:
        return None
    maximo = frutas[0]["precio"]
    for f in frutas:
        if f["precio"] > maximo:
            maximo = f["precio"]
    return maximo


# ----------------
# Programa principal (interactivo)
# ----------------
while True:
    print("\n--- FRUTERÍA ---")
    print("1. Añadir fruta")
    print("2. Buscar fruta")
    print("3. Ver precio medio")
    print("4. Ver precio máximo")
    print("5. Ver todas las frutas")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la fruta: ")
        try:
            precio = float(input("Precio (€): "))
            cantidad = float(input("Cantidad (kg): "))
        except ValueError:
            print("Error: precio o cantidad deben ser números.")
            continue
        agregar_fruta(frutas, nombre, precio, cantidad)

    elif opcion == "2":
        nombre = input("Introduce el nombre de la fruta que quieres buscar: ")
        resultado = buscar_fruta(frutas, nombre)
        if resultado:
            print("Fruta encontrada:", resultado)
        else:
            print("Esa fruta no está registrada.")

    elif opcion == "3":
        media = precio_medio(frutas)
        if media is not None:
            print("Precio medio:", media)
        else:
            print("No hay frutas registradas.")

    elif opcion == "4":
        maximo = precio_maximo(frutas)
        if maximo is not None:
            print("Precio máximo:", maximo)
        else:
            print("No hay frutas registradas.")

    elif opcion == "5":
        if len(frutas) == 0:
            print("No hay frutas guardadas.")
        else:
            print("Frutas registradas:")
            for f in frutas:
                print(f)

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
