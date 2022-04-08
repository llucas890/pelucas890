import os

direccion = input("Where is your file? Ex: C:/Users/file.txt\n")
direccion = direccion.replace('\\', "/")
abrir = open(direccion, "r+")
busqueda = str(input("What are you looking for: "))
for lin in abrir:
    if busqueda in lin:
        print(f"Found: '{busqueda}'")
        borrar = input(f"Want to remove the line? T o F: ")
        if borrar == "T":
            abrir.write(lin.replace(f"{busqueda}", ""))
            abrir.close()
            nuevoarchivo = input("New txt file to save search: ")
            direccion2 = open(f"E:/programa_txt/{nuevoarchivo}.txt", "w")
            direccion2.write(busqueda + os.linesep)
            direccion2.close()
            break
        else: 
            nuevoarchivo = input("New txt file to save search: ")
            direccion2 = open(f"E:/programa_txt/{nuevoarchivo}.txt", "w")
            direccion2.write(busqueda + os.linesep)
            direccion2.close()
else:
    print(f"Can't find {busqueda} in {direccion}. Exiting")