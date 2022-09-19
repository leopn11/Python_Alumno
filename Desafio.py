class Alumno:
    _nombre = None
    _nota = None
    def nombre(self):
        self._nombre = "Leo Pinto"


    def nota(self):
        self._nota = 100


a = Alumno()
a.nombre()
a.nota()
print("El alumno de la institución OpenBootcan", a._nombre, ", aprobó con una exelente calificacion de", a._nota, "puntos. En hora buena!")
