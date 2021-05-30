# importar librerias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
# se importa la clase(s) del archivo genera_tablas
from genera_tablas import Provincia,  Canton, Parroquia, Establecimiento

engine = create_engine('sqlite:///baseinstitucioneseducativas.db')

Session = sessionmaker(bind=engine)
session = Session()

# Abrir archivo csv
with open('data/Listado-Instituciones-Educativas.csv', 'r') as csv_file:
    # agregar en diccionario
    reader = csv.DictReader(csv_file, delimiter='|')
    lista = list(reader)
    datos = []
    for l in lista:
        # verifica si se repite
        if ([l['Código AMIE'],  l['Código División Política Administrativa  Parroquia'],
             l['Código de Distrito'], l['Nombre de la Institución Educativa'],
            l['Sostenimiento'], l['Tipo de Educación'],
            l['Modalidad'], l['Jornada'], l['Acceso (terrestre/ aéreo/fluvial)'],
                l['Número de estudiantes'], l['Número de docentes']]) not in datos:
            # si no se repite agrega en una lista valores unicos para proxima verificacion
            datos.append([l['Código AMIE'], l['Nombre de la Institución Educativa'],
                          l['Código de Distrito'], l['Sostenimiento'], l['Tipo de Educación'],
                          l['Modalidad'], l['Jornada'], l['Acceso (terrestre/ aéreo/fluvial)'],
                          l['Número de estudiantes'], l['Número de docentes']])
            # Agregar los datos
            agregar = Establecimiento(codigo=l['Código AMIE'], 
                codParroquia=l['Código División Política Administrativa  Parroquia'],
                distrito=l['Código de Distrito'], nombre=l['Nombre de la Institución Educativa'],
                sostenimiento=l['Sostenimiento'], tipoEducacion=l['Tipo de Educación'],
                modalidad=l['Modalidad'], jornada=l['Jornada'], 
                acceso=l['Acceso (terrestre/ aéreo/fluvial)'],
                numEstudiantes=l['Número de estudiantes'], 
                numDocentes=l['Número de docentes'])
            session.add(agregar)

# agregar
session.commit()
