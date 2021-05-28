# importar librerias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
# se importa la clase(s) del archivo genera_tablas
from genera_tablas import Provincia,  Canton #, Parroquia, Establecimiento

engine = create_engine('sqlite:///baseinstitucioneseducativas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Abrir archivo csv
with open('data/Listado-Instituciones-Educativas.csv', 'r') as csv_file:
    #agregar en diccionario
    reader = csv.DictReader(csv_file, delimiter='|')
    lista = list(reader)
    datos = []
    for l in lista:
        # verifica si se repite
        if [l['Código División Política Administrativa  Cantón'],l['Cantón'], l['Código División Política Administrativa Provincia']] not in datos:
            # si no se repite agrega en una lista valores unicos para proxima verificacion
            datos.append([l['Código División Política Administrativa  Cantón'],l['Cantón'], l['Código División Política Administrativa Provincia']])
            # Agregar los datos
            agregar = Canton(codigo=l['Código División Política Administrativa  Cantón'],  codProvincia=l['Código División Política Administrativa Provincia'], nombre=l['Cantón'])
            session.add(agregar)

# agregar 
session.commit()
