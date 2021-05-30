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
# Obtener consulta de establecimientos filtrando la provincia LOJA
consulta = session.query(Establecimiento).join(
    Parroquia, Canton, Provincia).filter(Provincia.nombre == 'LOJA').all()
# Recorre la lista obtenida
for c in consulta:
    print("Establecimiento: %s |Provincia: %s" %
          (c.nombre, c.parroquia.canton.provincia.nombre))
    i = i + 1

print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
# Obtener consulta de establecimientos filtrando la provincia LOJA y por Parroquia
consulta2 = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(\
    Provincia.nombre == 'LOJA', Canton.nombre == 'LOJA').all()
# Recorre la lista obtenida
for c2 in consulta2:
    print("Establecimiento: %s |Canton: %s |Provincia:%s" % (\
        c2.nombre, c2.parroquia.canton.nombre, c2.parroquia.canton.provincia.nombre))
    j = j + 1
print("-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-\t-x-")
print("Todos los establecimientos de la provincia de Loja\nResultados :%s" % (i))
print("Todos los establecimientos del cantón de Loja.\nResultados :%s" % (j))
