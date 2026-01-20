name = []
print(name)

#Metodo append para agregar elementos al final de la lista
name.append("Vharly")
name.append("Mar")
name.append("Alexis")
name.append("Erick")
name.append("Jona")
name.append("Arce")

print(name)
print(type(name))
print(len(name))

#Metodo insert para agregar un elementos en una posicion deseada
name.insert(1,"Hector")
print(name)

#Metodo pop() sin indice para eliminar unltimo elemento de la lista
name.pop()
print(name)

#Metodo pop() con indice para eliminar un elemento deseado
name.pop(2)
print(name)

#Metodo remove(val) para eliminar elementos por valor
name.remove("Vharly")
print(name)
