from Clases.alumno import Alumno
from Clases.profesor import Profesor

class Exalumno(Alumno,Profesor):
  def __init__(self):
    super().__init__()
    self.titulo=""

  def leerDatosExalumno(self):
    self.titulo = input("Título:")

  def mostrarDatosExalumno(self):
    print(self.titulo)