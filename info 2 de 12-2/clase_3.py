# clase de 12-4 del 24703/2026

class paciente:
    def __init__(self):
        self.__nombre:str
        self.__cedula:int = 123
        self.__eps:str 
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nCedula: {self.cedula}"
    
    def setNombre(self,n):
        self.__nombre = n
    
    def setCedula(self,n):
        self.__cedula = n
    
    def setEps(self,n):
        self.__eps = n
    
    def getNombre(self,):
        return self.__nombre 
    
    def getCedula(self):
        return self.__cedula 
    
    def getEps(self):
        return self.__eps  
    
    def setCedula(self,n):
        if isinstance (n,int):
            self.__cedula = n
        else:
            print (f"solo numeros enteros")
    
k = paciente()
k.nombre = "juan"
k.setCedula (12345)

print (k.getCedula())

class homosapiens ():
    pass
class Persona (homosapiens, paciente):
    def __init__(self) -> None :
        homosapiens.__init__()
        paciente.__init__(self)
print("hola mundo")