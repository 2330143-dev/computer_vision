from pathlib import Path 

BASE = Path(__file__).resolve().parent.parent
#parent sirve para engolobar como padre por lo cual lo ignorara como ruta
print (BASE)
#Muestra la carpeta del proyecto

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"

raw.mkdir(Parents=True, exist_ok = True)
clean.mkdir(Parents=True, exist_ok = True)

#Escribir a un archivo txt
txt_path = raw / "notas.txt"
txt_path.write_text("Mis alumnos favorito \n Hola chavos\n \t No van a reprobar", encoding="utf-8")

contenido = txt_path.read_text(encoding="tf-8")
print(contenido)
