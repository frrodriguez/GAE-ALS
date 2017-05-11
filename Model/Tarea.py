from Utils.Validation import ValidationObject
from google.appengine.ext import ndb

class Tarea(ndb.Model):
    estado = ndb.IntegerProperty(required=True)
    order = ndb.IntegerProperty(required=True, indexed=True)
    titulo = ndb.StringProperty(required=True)
    mensaje = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)


class TareaSchema:

    def __init__(self): #  Modifica el html generado para hacer corresponder el objeto con las restricciones HTML5
        self.titulo = ValidationObject("titulo").setIsRequired(True).setMinLength(3).setMaxLength(100)
        self.mensaje = ValidationObject("mensaje").setIsRequired(True).setMinLength(3).setMaxLength(500)

    def __getitem__(self, item):
        return {
            "titulo" : self.titulo,
            "mensaje" : self.mensaje
        }[item]




