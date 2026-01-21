def normalize_name(txt):
    """
    Esta función normaliza strings. Lo que hace es quitar
    los espacios en blanco al inicio y fin de misstring, 
    espacios en blanco los  elimina.
    Y el nombre en título

    Ej.
    CaRlOS AnToNio -> Carlos Antonio

    :params (str): texto de entrada
    :return: texto formateado
    """

    return " ".join(txt.strip().title().split()) # ["Calos","Antonio"]
def to_mxn(valor, tasa: float=1.0): #tasa -> Parametro opcional
    """
    Convierte un valor numerico a MXN multiplicando por la tasa
    """
    return float (valor)*float(tasa)
