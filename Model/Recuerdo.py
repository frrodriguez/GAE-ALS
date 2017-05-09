from Utils.Validation import ValidationObject
from google.appengine.ext import ndb

class Recuerdo(ndb.Model):
    mensaje = ndb.StringProperty(required=True)
    imagen = ndb.BlobProperty(required=True)
    user = ndb.StringProperty(required=True)
    fecha = ndb.DateTimeProperty(required=True, auto_now_add=True)


class RecuerdoSchema:

    def __init__(self): #  Modifica el html generado para hacer corresponder el objeto con las restricciones HTML5
        self.mensaje = ValidationObject("mensaje").setIsRequired(True).setMinLength(3).setMaxLength(100)
        self.imagen = ValidationObject("imagen").setIsRequired(True)

    def __getitem__(self, item):
        return {
            "mensaje" : self.mensaje,
            "imagen" : self.imagen
        }[item]




