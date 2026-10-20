print ("Registro de busqueda y ordenamiento ")

#Variable persona para almacenar las personas
ordenar = [5, 4, 3, 2, 1]
persona_lista = []
buscar = ["Persona1", "Persona2", "Persona3", "Persona4 "]

#Aca ponemos la lista de las opciones con un while true 
while True:
    print ("1 Registrar Persona")
    print ("2 Buscas persona    ")
    print ("3 Ordenar persona con numeros   ",ordenar)
    
    #Pedimos Al usuario que esta en el sistema que escoja una opcion    
    usuario = input ("Inidique una opcion   ")
    #Opcion 1
    if usuario == "1":
        nombre = input ("Escribe el nombre de la persona    ").strip()
        persona_lista.append (nombre)
        print ("Persona registrada el nombre es ",nombre)
    #Opcion 2
  
    elif usuario == "2":
        print (f"Nombre disponibles {buscar}    ")
        nombre = input ("¿Qué nombre quieres buscar ?   ")
        if nombre in buscar:
            print ("Persona Encontrada  ")
        else:
            print ("No se encontro  ")


    #Opcion 3
        
    elif usuario == "3":
        ordenar.sort()
        print ("Ordenado correctamente  ",ordenar)