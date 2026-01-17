name = "Hola Mundo"
print (name)

#Built-in method input (argument)
user_name = input ("¿Como te llamas:? ")
edad_txt = input ("¿Cuál es tu edad?: ")

#Built_in method type (1-argument)
print (user_name)
print (type(user_name))

print (edad_txt)
print (type(edad_txt))

#Método built-in int(1-argument)-comvierte un string a un número entero
try:
    edad = int(edad_txt)
    print(edad)
    print(type(edad))

except ValueError:
    print("Error: La conversió no se pudo realizar")
print("Pon un número entero")
print ("Fin del programa")