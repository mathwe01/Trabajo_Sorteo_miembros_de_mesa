continuar = True
def data_electores ():
    while continuar:
         dni = int(input("Escribe tu numero de DNI:  "))
         nombre = input ("Dijite su nombre:   ")
         apelldio = input ("Dijite su apellido:   ")
         firma = input ("Dijite su firma: ")
         print ("Genial su datos se han guardado correctamente: ")
         confirmacion = input ("¿Desea Registrar otros datos? (si/no)    ").lower()

         if confirmacion == "si":
              print ("Llena de vuelta el formulario:    ")
              continuar
         else:
              print ("Aca acaba el buclue   ")
              break

data_electores ()

