class Asignatura:

    def __init__(self, nombre, salon=None):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        salon = self._salon
        if salon is None:
            salon = "remoto"
        return self._nombre + " " + salon
