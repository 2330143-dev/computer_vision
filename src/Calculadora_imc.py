weigth_txt = input("Peso(Kg): ")
heigth_txt = input("Altura(M): ")

try:
    weigth = float(weigth_txt)
    heigth = float(heigth_txt)
    imc = weigth / heigth**2
    print(f"Tu IMA es {imc}")

except ValueError:
    print("Datos invalidos. Ej.: peso 70.5, altura 1.75")
except ZeroDivisionError: 
    print("Error. No está permitida la división por cero")
except Exception as err:
    print(err)

#print(f"Tu IMC es {imc}")
