# clase 3 del 24/02/2026
class perro:
    def __init__(self):
        self.__raza:str
        self.__edad:int = 23
        self.__idt:int
        self.__nombre:str
        
    def __str__(self):
        return f"Nombre: {self.nombre}\n ID:{self.idt}"
    
    def hacerRuido(self):
        print(f"{self.nombre} Ladra")
        
        
    def setNombre(self,n):
        self.__nombre = n
    def setID(self,n):
        self.__idt = n
    def setRaza(self,n):
        self.__raza = n
    
    def setEdad(self,n):
        self.__edad = n
    
    def getombre(self,n):
        return self.__nombre 
    def getID(self,n):
        return self.__idt 
    def getRaza(self,n):
        return self.__raza 
    def getEdad(self,n):
        return self.__edad 
    
        
        
    def asignar_Edad(self,e):
        if isinstance(e,int):
            self.__edad = e
        else:
            print ("solo valores numericos")
            
    def asignar_Nombre(self,e):
        if isinstance(e,str):
            self.__nombre = e
        else:
            print ("solo valores Alfabeticos")
            
    def asignar_Raza(self,e):
        if isinstance(e,str):
            self.__raza = e
        else:
            print ("solo valores Alfabeticos")
            
    def asignar_ID(self,e):
        if isinstance(e,str):
            self.__idt = e
        else:
            print ("solo valores Numericos")
            
            
class Gato (perro):
    def __init__(self):
        super().__init__(self)
        
    def hacerRuido(self):
        print(f"{self.nombre} Maulla")
        

g = perro()
g.asignar_Nombre= "firulais"
g.asignar_Edad = "doce"
g.asignar_ID= 123
g.asignar_Raza= "Criollo"
print(g.nombre)
print("hola mundo")