# Clase 2 del 19/02/2026

class pcmasterrace:
    def __init__(self, m ,p ,mod, pre)-> None:
        self.Marca: str = m
        self.Procezadores: str = p
        self.Modelo: str = mod
        self.Precio: float = pre
    
    def verificar(self, b):
        if b == True:
            print("el procezador es tuyo")
        else:
            print("el procezador no es tuyo")
            
j =[]
for i in range(4):
    m = input("Marca: ")
    p = input("Procezador: ")
    mod = input("Modelo: ")
    pre = int(input("Precio: "))
    j.append(pcmasterrace(m ,p ,mod, pre))

print(j[0])
