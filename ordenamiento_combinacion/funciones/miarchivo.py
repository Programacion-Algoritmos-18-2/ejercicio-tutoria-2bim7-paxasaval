import codecs
import sys


class MiArchivo:
    """
    """
    
    def __init__(self, nombre):
        """
        """
        self.nombre_archivo = nombre 
        self.archivo = codecs.open(self.nombre_archivo, "r")


    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()
