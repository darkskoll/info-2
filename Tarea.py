class Pacientes():
    def __init__(self):
        self.__Nombre = ""
        self.__Cedula = 0
        self.__Genero = ""
        self.__Servicio = ""
    
    def verNombres(self):
        return self.__Nombre
    def verCedula(self):
        return self.__Cedula
    def verGenero(self):
        return self.__Genero
    def verServicio(self):
        return self.__Servicio
    
    def asignarNombre(self,n):
        self.__Nombre = n
    def asignarCedula(self,c):
        self.__Cedula = c
    def asignarGenero(self,g):
        self.__Genero = g
    def asignarServicio(self,s):
        self.__Servicio = s

class Sistema:
    def __init__(self):
        self.__lista_pacientes = []
        
        self.__numero_