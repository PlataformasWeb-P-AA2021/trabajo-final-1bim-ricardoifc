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
# Obtener consulta de Los establecimientos ordenados por nombre de parroquia que tengan más de 20
#  profesores y la cadena'Permanente' en tipo de educación.
consulta = session.query(Establecimiento).join(Parroquia).order_by(Parroquia.nombre).filter(
    Establecimiento.numDocentes > 20, Establecimiento.tipoEducacion.like("%Permanente%")).all()

# Recorre la lista obtenida
for c in consulta:
    print("Parroquia: %s|Establecimiento: %s|Tipo de educacion: %s|Docentes: %s" %
          (c.parroquia.nombre, c.nombre, c.tipoEducacion, c.numDocentes))
    i = i + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
# Obtener consulta de Todos los establecimientos ordenados por sostenimiento y tengan código de
#  distrito 11D02.
consulta2 = session.query(Establecimiento).order_by(
    Establecimiento.sostenimiento).filter(Establecimiento.distrito == '11D02').all()
# Recorre la lista obtenida
j = 0
for c2 in consulta2:
    print("|Sostenimiento: %s|Establecimiento: %s|Distrito: %s" % (
        c2.sostenimiento, c2.nombre, c2.distrito))
    j = j + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
print("Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y\
     la cadena'Permanente' en tipo de educación.\nResultados :%s" % (i))
print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.\
    \nResultados :%s" % (j))
