print("Este programa captura importes")
info = """
      Este programa lleva el conteo de cuantos importes ha 
      introducido un usuario
      
      va acumulando todos los importes que el usuario ingresa.

      Si el usuario decea terminar el programa puede escribir
      en cualquier momento la palabra exit, quit,terminar.

      Elaborado por Mar
"""
print(info)
conteo = 0
suma = 0.0
minimo = None
maximo = None


while True:
    user_message = """
Ingresa tu importe (MXN)
si quieres dejar de capturar importes
puedes ingresar en cualquier momento
exit, quit, terminar.
"""
    line = input(user_message).lower()
    if line == "exit" or line == "quit" or line == "terminar":
          break
    try:
        value = float(line)

    except ValueError:
        print("Valor invalido. Intente de nuevo (ej. 125.5)")
        continue

    conteo+= 1 # Dice cuantos números an sido ingresados
    suma+= value # Me lleva la acumulación
    if minimo is None or value < minimo:
        minimo = value
    if maximo is None or value > maximo:
        maximo = value

    if conteo == 0:
        print("No se capturaron importes")
    else:
        print("="*32)
        print (f"{conteo}")
        print(f"{suma}")
        print(f"{minimo}")
        print(f"{maximo}")
    print("")
    
print("Programa finalizado")
