# versión con manejo de errores

def media(precios):
    try:
        if len(precios) == 0:
            raise ValueError("Lista vacía")
        return sum(precios) / len(precios)
    except TypeError:
        print("Error: la lista contiene elementos no numéricos.")
    except ValueError as e:
        print("Error:", e)
    finally:
        pass

def maximo(precios):
    try:
        return max(precios)
    except ValueError:
        print("Error: lista vacía.")
    except TypeError:
        print("Error: elementos no válidos.")
    finally:
        pass

def minimo(precios):
    try:
        return min(precios)
    except ValueError:
        print("Error: lista vacía.")
    except TypeError:
        print("Error: elementos no válidos.")
    finally:
        pass
