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
# Obtener consulta de cantones con 0 profesores en establecimientos
consulta = session.query(Establecimiento).filter(
    Establecimiento.numDocentes == 0).all()

# Recorre la lista obtenida
for c in consulta:
    print("Caton: %s |Establecimiento: %s |Profesores: %s" %
          (c.parroquia.canton.nombre, c.nombre, c.numDocentes))
    i = i + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
# Obtener consulta de la parroquia catacocha con estudiantes mayores o igual a 21
consulta2 = session.query(Establecimiento).join(
    Parroquia).filter(Parroquia.nombre == 'CATACOCHA', Establecimiento.numEstudiantes \
        >= 21).all()
# Recorre la lista obtenida
j = 0
for c2 in consulta2:
    print("parroquia: %s |Establecimiento: %s |Numero de estudiantes: %d" % (
        c2.parroquia.nombre, c2.nombre, c2.numEstudiantes))
    j = j + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
print("Los cantones que tiene establecimientos con 0 número de profesores\nResultados \
    :%s" % (i))
print("Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes \
    mayores o iguales a 21\nResultados :%s" % (j))
