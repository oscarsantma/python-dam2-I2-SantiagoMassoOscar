import datetime  # Para registrar la fecha de la tarea

# Lista donde se guardan las tareas
tareas = []

# --- FUNCIONES ---

def agregar_tarea(lista, descripcion):
    """Agrega una nueva tarea con fecha actual y estado pendiente."""
    # Obtenemos la fecha de hoy
    fecha = datetime.date.today()
    
    # Creamos cada parte de la tarea
    tarea_descripcion = descripcion
    tarea_fecha = fecha
    tarea_completada = False
    
    # Creamos el diccionario de la tarea
    tarea = {
        "descripcion": tarea_descripcion,
        "fecha": tarea_fecha,
        "completada": tarea_completada
    }
    
    # Añadimos la tarea a la lista
    lista.append(tarea)
    
    return "Tarea agregada correctamente."


def mostrar_tareas(lista):
    """Muestra todas las tareas con su estado y fecha de creación de forma sencilla."""
    if len(lista) == 0:
        return "No hay tareas registradas."
    
    texto = ""
    for i in range(len(lista)):
        tarea = lista[i]
        
        # Estado de la tarea
        if tarea["completada"]:
            estado = "✅ Completada"
        else:
            estado = "⏳ Pendiente"
        
        # Desglosamos la línea en partes más simples
        indice = str(i)
        descripcion = tarea["descripcion"]
        fecha = str(tarea["fecha"])
        
        linea = indice + ". " + descripcion + " - " + estado + " (Agregada: " + fecha + ")\n"
        
        # Añadimos la línea al texto completo
        texto += linea
    
    return texto


def completar_tarea(lista, indice):
    """Marca una tarea como completada."""
    try:
        lista[indice]["completada"] = True
        return "Tarea marcada como completada."
    except IndexError:
        return "Error: ese número de tarea no existe."
    except:
        return "Error desconocido."


# --- PROGRAMA PRINCIPAL ---
seguir = True
while seguir:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        desc = input("Escribe la tarea: ")
        print(agregar_tarea(tareas, desc))

    elif opcion == "2":
        print(mostrar_tareas(tareas))

    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para completar.")
        else:
            # Mostramos las tareas primero para que el usuario vea los números
            print(mostrar_tareas(tareas))
            try:
                num = int(input("Número de la tarea a completar: "))
                print(completar_tarea(tareas, num))
            except ValueError:
                print("Por favor, escribe un número válido.")

    elif opcion == "4":
        print("¡Hasta luego!")
        seguir = False

    else:
        print("Opción no válida. Inténtalo de nuevo.")
