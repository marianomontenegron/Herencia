from Clases.exalumno import Exalumno

def main():
    exalumno = Exalumno()
    exalumno.leerDatosPersona()
    exalumno.leerDatosAlumno()
    exalumno.leerDatosExalumno()
    exalumno.leerDatosProfesor()

    exalumno.mostrarDatosPersona()
    exalumno.mostrarDatosAlumno()
    exalumno.mostrarDatosExalumno()
    exalumno.mostrarDatosProfesor()


if __name__ == '__main__':
    main()