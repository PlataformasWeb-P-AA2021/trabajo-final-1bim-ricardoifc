# Trabajo Final Primer Bimestre

## Documentación
### Las tablas son las siguientes
* #### Tabla provincia
*   codigo: (String) Clave primaria
*   nombre: (String)

* #### Tabla canton
*   codigo: (String)Clave Primaria
*   codProvincia: (String)Clave foranea de Provincia
*   nombre: (String)

* #### Tabla parroquia
*   codigo: (String) Clave Primaria
*   codCanton: (String) Clave foranea de Canton
*   nombre: (String)

* #### Tabla establecimiento
*   codigo: (String) Clave Primaria
*   codParroquia: (String) Clave foranea de Parroquia
*   distrito: (String)
*   nombre: (String)
*   sostenimiento: (String)
*   tipoEducacion: (String)
*   modalidad:(String)
*   jornada: (String)
*   acceso: (String)
*   numEstudiantes: (Entero)
*   numDocentes: (Entero)
### Motor de base de datos
* sqlite
### Librerias usadas
* sqlalchemy
* csv
### Para ingreso de datos
* Los datos se encuentran en la carpeta "data" donde encontramos el archivo .csv
* Para el ingreso de estos datos es necesario abrir el archivo y delimitar por "|"
* despues de obtener diccionarios se agrega a una lista y se comprueba que los datos no esten duplicados 
## Orden de ejecucion:
* genera_tablas.py
* ingresa_provincias.py
* ingresa_cantones.py
* ingresa_parroquias.py
* ingresa_establecimientos.py
* consulta1.py
* consulta2.py
* consulta3.py
* consulta4.py
* consulta5.py
