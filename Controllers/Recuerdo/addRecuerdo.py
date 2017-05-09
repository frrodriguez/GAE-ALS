from Controllers.BaseController.baseController import BaseHandler

import time

import json

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Utils.validateUserInput import ValidateInput

from Model.Recuerdo import Recuerdo
from Model.Recuerdo import RecuerdoSchema

class CrearRecuerdoHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"CrearRecuerdo")
        print ("INIT")
        print (self.request)


    def get(self):
        wrapEntidadesSchema(self,"Recuerdo")

        template = self.get_template( "index.html")
        self.response.write(template.render(self.render_data))


    def post(self):
        schema = RecuerdoSchema()
        errors = ValidateInput(self, schema["mensaje"])

        image_file = self.request.get("imagen", None)
        if (image_file == None):
            self.render_data["errors"].update({
                "imagen" : { "type" : "REQUIRED"}
            })

        if errors:
            wrapEntidadesSchema(self, "Recuerdo")
            self.render_data.update({
                "recuerdo": {
                    "mensaje": self.request.get("mensaje", ""),
                }
            })
            self.render_data["errors"].update(errors)

            template = self.get_template("index.html")
            self.response.write(template.render(self.render_data))
            return

        recuerdo = Recuerdo(mensaje=self.mensaje,
                            imagen=image_file,
                            user=self.user.get_id())
        recuerdo.put()
        time.sleep(1)
        self.redirect('/recuerdos')
