class Recordatorio:
    def __init__(self,tipo=0,titulo="",materia="",fecha="",hora="",descripcion=""):
        self.tipo= tipo
        self.titulo= titulo
        self.materia= materia
        self.fecha= fecha
        self.hora= hora
        self.descripcion= descripcion
    
    #mostrar datos de recordatorio
    def mostrar(self):
        print("Titulo: ",self.titulo)
        if(self.tipo==0):
            print("Materia: ",self.materia)
        print("Fecha: ",self.fecha)
        print("Hora: ",self.hora)
        print("Descripcion: ",self.descripcion)
    
    def to_json(self):
        return {
            "tipo" : self.tipo,
            "titulo" : self.titulo,
            "materia" : self.materia,
            "fecha" : self.fecha,
            "hora" : self.hora,
            "descripcion" : self.descripcion
        }
    #__str__?
    #to json?

    #getters y setters
    
    def getTipo(self):
        return self.tipo
    def setTipo(self,value):
        self.tipo = value
        
    def getTitulo(self):
        return self.titulo
    def setTitulo(self,value):
        self.titulo = value

    def getMateria(self):
        return self.materia
    def setMateria(self,value):
        self.materia = value
    
    def getFecha(self):
        return self.fecha
    def setFecha(self,value):
        self.fecha = value
        
    def getHora(self):
        return self.hora
    def setHora(self,value):
        self.hora = value
    
    def getDescripcion(self):
        return self.descripcion
    def setDescripcion(self,value):
        self.descripcion = value
            
    