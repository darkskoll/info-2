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
        self.__lista_pacienta = []
        
        self.__numero_pascientes = len(self.__lista_pacientes)
        
    def ingresarPacientes(self):
        Nombre = input("ingrese Nombre delñ paciente: ")
        Cedula = int(input("Ingrese la cedulña del paciente: "))
        Genero = input("ingrese el genero del paciente: ")
        Servicio = input("Ingrese el servicio: ")
        
        P = Pacientes()
        P.asignarNombre(Nombre)
        P.asignarCedula(Cedula)
        P.asignarGenero(Genero)
        P.asignarServicio(Servicio)
        
        self.__lista_pacienta.append(P)
        
        self.__numero_pascientes = len(self.__lista_pacientes)
        
    def VerNumeroPacientes(self):
        return self.__numero_pascientes
    def VerDatosPacientes(self):
        for i in self.__lista_pacienta:
            if  Cedula == Pacientes.verCedula():
                print("Nombre: " + Pacientes.verNombres())
                print("Cedula: " + str(Pacientes.verCedula()))
                print("Genero: " + Pacientes.verGenero())
                print("Servicio: " + Pacientes.verServicio())
                
mi_sistema = Sistema()

while True:
    opcion = int(input("1. Ingresar paciente - 2. Ver numero de pacientes - 3. Ver datos de paciente - 4. Salir"))
    if opcion == 1:
        mi_sistema.ingresarPacientes()
    elif opcion == 2:
        print("Ahora hay " + str(mi_sistema.VerNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.VerDatosPacientes()
    elif opcion ==4:
        break
    else:
        print("Opcion no valida")