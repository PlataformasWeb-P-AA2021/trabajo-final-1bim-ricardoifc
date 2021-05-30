from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Provincia,  Canton, Parroquia, Establecimiento

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///baseinstitucioneseducativas.db')
Session = sessionmaker(bind=engine)
session = Session()
i = 0
j = 0
# Obtener consulta de Establecimientos filtrados por jornada Nocturna
consulta = session.query(Establecimiento).filter(
    Establecimiento.jornada == 'Nocturna').all()

# Recorre la lista obtenida
for c in consulta:
    print("Parroquia: %s |Jornada: %s |Establecimiento: %s" %
          (c.parroquia.nombre, c.jornada, c.nombre))
    i = i + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
# Obtener consulta de cantones con numero de estudiantes especificos
consulta2 = session.query(Establecimiento).filter(or_(Establecimiento.numEstudiantes == 448,\
    Establecimiento.numEstudiantes == 450, Establecimiento.numEstudiantes == 451, \
    Establecimiento.numEstudiantes == 454, Establecimiento.numEstudiantes == 558, \
    Establecimiento.numEstudiantes == 459, )).all()
# Recorre la lista obtenida
j = 0
for c2 in consulta2:
    print("Canton: %s |Establecimiento: %s |Numero de estudiantes: %s" % (
        c2.parroquia.canton.nombre, c2.nombre, c2.numEstudiantes))
    j = j + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
print("Las parroquias que tienen establecimientos únicamente en la jornada Nocturna\
    \nResultados :%s" % (i))
print("Los cantones que tiene establecimientos como número de estudiantes tales como:\
     448, 450, 451, 454, 458, 459.\nResultados :%s" % (j))
