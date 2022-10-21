import json

""" Ejemplo de un elemento de la lista "contactos"
"Materia": "",
"Hora Inicial": "",
"Hora Final": "",
"Dia Inicial": "",
"Dia Final": "",
"Seccion": "",
"""

#Esta es nuestra base para el JSON vacío
usuario = '''{
    "asignaturas": [
    ]
}
'''

#Con esto recargamos el formato vacío a un archivo JSON
data = json.loads(usuario)
print(data)
dpro = json.dumps(data, indent=2)

with open("Usuario1.json", 'w') as file:
    file.write(dpro)
    file.close()


#Pruebas de integridad cargando desde el JSON
with open("Usuario1.json", 'r') as file:
    #print(file["contactos"])
    usuario = json.load(file)
    file.close()

#print(type(usuario))

#contactos = usuario["contactos"]
#contactos.append({"nombre": "Juan"})
#usuario["contactos"].append({"nombre": "Juan"})
#for contacto in usuario["contactos"]:
#    print(contacto["nombre"])

#Reguardo para ver cambios luego de algún test
dump = json.dumps(usuario, indent=2)
with open("Usuario1.json", 'w') as file:
    file.write(dump)
    file.close()