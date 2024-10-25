print (" ") #Esta linea da el espacio para el nombre
print ("Cristian David Salas De La O 3-W") # Esta linea muestra el nombre 
print (" ") #Esta linea da el espacio para el nombre
f = open("demofile.txt", "r") #Esta linea define como abrir el archivo

content = f.read() #Esta linea define el contenido 

print(content) #Esta linea muestra el contenido

f.close() #Esta linea cierra todo
