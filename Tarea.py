from py_compile import main


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
<<<<<<< HEAD
        
        self.__numero_
=======
    def ingresarPacientes(self,pac):
        self.__lista_pacientes.append(pac)
    def VerDatosPacientes(self,c):
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    def VerNumeroPacientes(self):
        print("En la lista hay " + str(len(self.__lista_pacientes)) + " pacientes")
        
    def main():
        sis = Sistema()
        
        while True:
            opcion = int(input("Ingrese 0 para salir, 1 para ingresar nuevo paciente, 2. ver paciente: "))
            if opcion == 1:
                print("A continuacion se solicintan los datos ...")
                Nombre = input("ingrese Nombre delñ paciente: ")
                Cedula = int(input("Ingrese la cedulña del paciente: "))
                Genero = input("ingrese el genero del paciente: ")
                Servicio = input("Ingrese el servicio: ")
                
                pac = Pacientes()
                pac.asignarNombre(Nombre)
                pac.asignarCedula(Cedula)
                pac.asignarGenero(Genero)
                pac.asignarServicio(Servicio)
                
                sis.ingresarPacientes(pac)
                
            elif opcion == 2:
                c = int(input("Ingrese la cedula del paciente a buscar: "))
                p = sis.VerDatosPacientes(c)
                print("Nombre: " + p.verNombres())
                print("Cedula: " + str(p.verCedula()))
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
            elif opcion !=0:
                continue
            else:
                break
        
    if __name__ == "__main__":
        main()
>>>>>>> b0c6abf4416353c535a009cdf552f0bb7667046b
