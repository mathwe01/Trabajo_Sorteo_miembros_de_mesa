import random 

miembro = ["mesa 1", "mesa 2", "mesa 3", "mesa 4"]

sorteo = random.choice (miembro)
while True:
    usuario = input ("Elige un miembro de mesa:  ")

    if usuario == "mesa 1":
        print ("Ese miembro de mesa ya fue escogido ")
    elif usuario == "mesa 2":
        print ("mienbro de mesa a un no escogido ")
    elif usuario == "mesa 3":
        print ("mienbro de mesa a un no escogido    ")
    elif usuario == "mesa 4":
        print ("mienbro de mesa a un no escogido    ")
    else:
        print ("No se escogio nigun miembro de mesa ")