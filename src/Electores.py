


def crear_electores ():
    dni = int(input("Introdusca su numero de DNI    "))
    nombre = input ("Introduzca su nombre   ")
    edad = int(input("Introdusca su edad    "))
    mesa = int(input("Introdusca el numero de mesa  "))
    instruccion = int(input("Introdusca su numero de instruccion    "))
    veces = int(input("Introdusca su numero de veces que estas participando    "))
    observador = int(input("Numero de veces que fue observado   "))
    return ()

crear_electores ()

def registrar_elector ():
    dni = int(input("Vuelva Introducir de vuelta su numero de DNI   "))
    elector_nuevo = int(input("Introduzca su nuevo numero de elector    "))

    if elector_nuevo == dni:
        print (False)
        print ("Ese numero de DNI ya se ha registrado ")
    elif elector_nuevo != dni:
        print (True)
        print ("Puedes usar ese nuevo elector porque no se ha registrado    ")
    else:
        print ("No se registro nuevo elector    ")

registrar_elector ()

buscar = 123456789

def buscar_secuencial():


    dni = int(input("Introdusca el numero de DNI   "))
    if dni == buscar:
        print ("Se encontro la secuencial   ")
    elif dni != buscar:
        print ("No se encontro  ")

        

buscar_secuencial()
 

 


    


    
    