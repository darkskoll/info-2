from Clase_7_EEG import *
def main ():
    sis = Sistema()
    while True:
        Cedula = validar("Ingrese la cedula: ")
        if sis.verificarExiste(Cedula) == True:
            print(f"Paciente ya esta en el sistema... verifique la cedula del paciente")
            continue
        else:
                p=Paciente()
                p.AsignarNombre(input("Nombre: "))
                p.asignarCedula(Cedula)
                p.asignarGenero(input("Género: "))
                numVis =  validar (f"Ingrese la cantidad de visitas que va ingresar del paciente {p.verNombre()}: ")
                for i in range(0,numVis):
                    dia = validar("Ingrese dia:")
                    mes = validar("Ingrese mes:")
                    año = validar("Ingrese año:")
                    f = datetime.datetime(año, mes, dia).strftime("%x")
                    if p.verificarExiste(f) == True:
                        print("Ya existe  visita, ingrese otra porfavor")
                        continue
                    
                    v = Visita()
                    v.asignarFecha(f)
                    v.asignarRegistro(f'Pacientes_{p.verCedula()}')
                    v.asignarNotas(input("Ingrese Observaciones: "))
                    ind=v.verIndice()
                    ind.asignarPot_A1(validarf("Ingrese a1= "))
                    ind.asignarPot_A2(validarf("Ingrese a2= "))
                    ind.asignarPot_B(validarf("Ingrese b= "))
                    ind.asignarPot_D(validarf("Ingrese d= "))
                    ind.asignarPot_G(validarf("Ingrese g= "))
                    ind.asignarPot_T(validarf("Ingrese t= "))
                    # v.asignarIndice(ind)
                    p.ingresarVistas(v)
                    
                sis.ingresarPac(p)
                
        elif valor == 2: #Edición de Paciente
            cedula = validar("Ingrese Cedula")
            if sis.verificarExiste(cedula):
                pac= sis.verPac(Cedula)