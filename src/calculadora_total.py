#Este programa pide al usuario una cantidad
subtotal_txt = input ("subtotal(mxn): ")
iva_txt = input ("Iva(%) ej.16: ")
propina_txt = input ("propina(%) ej.10: ")

#Metodo built-in float-Convierte a un dato de tipo flotante
try:
    subtotal = float (subtotal_txt)
    iva = float (iva_txt)/100
    propina = float (propina_txt)/100

except ValueError:
    print ("Entrada invalida: utiliza números")
    exit(1)

monto_iva = subtotal*iva
monto_propina = subtotal*propina
total = subtotal+monto_iva+monto_propina

print(f"subtotal: {subtotal}")
print(f"Iva: {monto_iva}")
print(f"propina: {monto_propina}")
print (f"Total: {total}")
