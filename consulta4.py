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
# Obtener consulta de establecimientos ordenados por numero de estudiantes y tengan
#  mas de 100 profesores
consulta = session.query(Establecimiento).order_by(Establecimiento.numEstudiantes).\
    filter(Establecimiento.numDocentes >= 100).all()

# Recorre la lista obtenida
for c in consulta:
    print("Establecimiento: %s |Profesores: %s|Estudiantes: %s" %
          (c.nombre, c.numDocentes, c.numEstudiantes))
    i = i + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
# Obtener consulta de establecimientos ordenados por numero de profesores y tengan
#  mas de 100 profesores 21
consulta2 = session.query(Establecimiento).order_by(Establecimiento.numDocentes).\
    filter(Establecimiento.numEstudiantes >= 100).all()
# Recorre la lista obtenida
j = 0
for c2 in consulta2:
    print("|Establecimiento: %s|Estudiantes: %s|Profesores: %s" % (
        c2.nombre, c2.numEstudiantes, c2.numDocentes))
    j = j + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 \
    profesores.\nResultados :%s" % (i))
print("Los establecimientos ordenados por número de profesores; que tengan más de 100 \
    profesores.\nResultados :%s" % (j))
