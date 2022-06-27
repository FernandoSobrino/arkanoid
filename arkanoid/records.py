class Records:
    def __init__(self):
        """
        En el constructor, quiero crear los atributos para la ruta y
        comprobar si el archivo existe.
        """
        pass

    def insertar_record(self,nombre:str,puntos:int):
        """
        Agrega un registro en el listado de records con el nombre
        del jugador y los puntos conseguidos.
        La lista de records se debe quedar ordenada. Es decir,
        se inserta en la posición que toca ordenando de mayor a menor.
        """
        pass

    def obtener_puntuacion_menor(self):
        """
        Devuelve un entero con el valor de puntos de la última
        posición del listado de records.
        """
        pass

    def guardar_records(self):
        """
        guarda el archivo de records.
        """
        pass

    def cargar_records(self):
        """
        carga el archivo de records si existe.
        """
        pass

    def reset(self):
        """
        vaciar el archivo de records
        """
        pass