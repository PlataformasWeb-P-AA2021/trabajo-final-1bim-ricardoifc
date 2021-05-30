# importar librerias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///baseinstitucioneseducativas.db')
Base = declarative_base()

# Crear la tabla de provincias
class Provincia(Base):
    __tablename__ = 'provincia'
    codigo = Column(String(2),primary_key=True)
    nombre = Column(String(40))
    canton = relationship("Canton", back_populates="provincia")
    def __repr__(self):
        return "Provincia: codigo=%s nombre=%s" % (
                          self.codigo, 
                          self.nombre)

# Crear la tabla de cantones
class Canton(Base):
    __tablename__ = 'canton'
    codigo = codigo = Column(String(4),primary_key=True)
    codProvincia = Column(String(2), ForeignKey('provincia.codigo'))
    nombre = Column(String(40))
    provincia = relationship("Provincia", back_populates="canton")
    parroquia = relationship("Parroquia", back_populates="canton")
    def __repr__(self):
        return "Canton: codigo: %s - codProvincia: %s - nombre: %s " % (
                self.codigo,
                self.codProvincia,
                self.nombre)


# Crear la tabla de parroquias
class Parroquia(Base):
    __tablename__ = 'parroquia'
    codigo = Column(String(6),primary_key=True)
    codCanton = Column(String(4), ForeignKey('canton.codigo'))
    nombre = Column(String(40))
    canton = relationship("Canton", back_populates="parroquia")
    establecimiento = relationship("Establecimiento", back_populates="parroquia")
    def __repr__(self):
        return "Parroquia: codigo: %s - codCanton:%s - nombre: %s" % (
                self.codigo,
                self.codCanton,
                self.nombre)


# Crear la tabla de establecimientos
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    codigo = Column(String(8),primary_key=True)
    codParroquia = Column(String(6), ForeignKey('parroquia.codigo'))
    distrito = Column(String(5))
    nombre = Column(String(40))
    sostenimiento = Column(String(13))
    tipoEducacion = Column(String(18))
    modalidad = Column(String(50))
    jornada = Column(String(40))
    acceso = Column(String(9))
    numEstudiantes = Column(Integer)
    numDocentes = Column(Integer)
    
    parroquia = relationship("Parroquia", back_populates="establecimiento")
    def __repr__(self):
        return "Establecimiento: codigo: %s - codParroquia:%s - distrito:%s - nombre: %s\
             - sostenimiento: %s - tipoEducacion: %s - modalidad: %s - jornada: %s\
                  - acceso: %s - numEstudiantes: %d - numDocentes: %d" % (
                self.codigo, self.codParroquia, self.distrito, self.nombre,
                self.sostenimiento, self.tipoEducacion, self.modalidad, self.jornada,
                self.acceso, self.numEstudiantes, self.numDocentes)

Base.metadata.create_all(engine)
