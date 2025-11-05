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
        if f["nombre"] == nombre:
            print("Error: esa fruta ya existe.")
            return

    nueva = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    frutas.append(nueva)
    print("Fruta añadida correctamente.")


# Buscar fruta por nombre
def buscar_fruta(frutas, nombre):
    for f in frutas:
        if f["nombre"] == nombre:
            return f
    return None


# Calcular estadística: precio medio de todas las frutas
def precio_medio(frutas):
    if len(frutas) == 0:
        return None

    total = 0
    for f in frutas:
        total += f["precio"]

    return total / len(frutas)


# ----------------
# Ejemplo de uso
# ----------------
agregar_fruta(frutas, "Manzana", 2.5, 10)
agregar_fruta(frutas, "Plátano", 1.8, 8)
agregar_fruta(frutas, "Manzana", 3.0, 5)   # Duplicado → error

print("Buscar plátano:", buscar_fruta(frutas, "Plátano"))
print("Precio medio:", precio_medio(frutas))
