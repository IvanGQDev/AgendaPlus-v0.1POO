from recordatorio import Recordatorio
import json

class AdministraRecordatorio():
    def __init__(self):
        self.recordatorios = []
        #como hago jalar el diccionario?
        self.dicRecordatorios = {}
    
    def __len__(self):
        return len(self.recordatorios)

    def ordenar(self):
        self.recordatorios.sort(key=lambda x: x.getFecha())

    def nuevoRecordatorio(self,recordatorio):
        self.recordatorios.append(recordatorio)
        self.ordenar()
        #ordenar por fecha tal vez?
    
    def modificarRecordatorio(self,id,recordatorio):
        self.recordatorios[id] = recordatorio
        #ordenar
    
    def eliminarRecordatorio(self,id):
        self.recordatorios.pop(id)
    
    def mostrarRecordatorios(self):
        for i in self.recordatorios:
            i.mostrar()

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                listaRecordatoriosJson =[recordatorio.to_json() for recordatorio in self.recordatorios]
                json.dump(listaRecordatoriosJson ,archivo, indent = 4)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                listaDirectorios = json.load(archivo)
                self.recordatorios = [Recordatorio(**recordatorio) for recordatorio in listaDirectorios]
            return 1
        except:
            return 0

