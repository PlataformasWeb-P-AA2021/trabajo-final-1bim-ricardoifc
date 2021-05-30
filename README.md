# Trabajo Final Primer Bimestre

## Documentación

* ### Tabla Provincia
*   codigo: Clave primaria
*   nombre
*   
* ### Tabla Canton
*   codigo: Clave Primaria
*   codProvincia: Clave foranea de Provincia
*   nombre
*   
* ### Tabla Parroquia
*   codigo: Clave Primaria
*   codCanton: Clave foranea de Canton
*   nombre
*   
* ### Tabla Establecimiento
*   codigo: Clave Primaria
*   codParroquia: Clave foranea de Parroquia
*   distrito
*   nombre
*   sostenimiento
*   tipoEducacion
*   modalidad
*   jornada
*   acceso
*   numEstudiantes
*   numDocentes
*   
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
