# clase de 12, 19/02/2026

class celular:
    def __init__(self,marca , modelo, año)-> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.año: int = año
    
    def verificar(self):
        if self.año <= 2024:
            print ("no comprar")
        elif self.año > 2024:
            print ("se puede comprar")
            
    def funcion(self, b):
        if b:
            print ("si llama")
        else:
            print ("no llama")
    pass

k =[]
for i in range(3):
    mar = input("marca del celular: ")
    mod = input("modelo del celular: ")
    an = int(input("año del celular: "))
    k.append(celular(mar ,mod ,an ))
    # o crear una variable y guardar las de mas variale y luego agragar a a lista
print(k[1])

q = int(input("llama 1.si o 0.no "))
k[1].funcion(q)