from Controllers.BaseController.baseController import BaseHandler

import time

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Utils.validateUserInput import ValidateInput
from Utils.Validation import ValidationObject

from Model.Tarea import Tarea
from Model.Tarea import TareaSchema

from google.appengine.ext import ndb

class EditarTareaHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"EditarTarea")
        print ("INIT")
        print (self.request)


    def get(self):

        errors = ValidateInput(self, ValidationObject("Tareakey").setIsRequired(True))
        wrapEntidadesSchema(self,"Tarea")

        if errors :
            if "Tareakey" in errors:
                self.error(402)
                return

        tareaKey = ndb.Key(urlsafe=self.Tareakey)
        tarea = tareaKey.get()

        if not tarea:
            self.error(404)
            return

        if self.user.get_id() != tarea.user:
            self.error(401)
            return

        self.render_data.update({
            "tarea" : tarea
        })

        template = self.get_template( "index.html")
        self.response.write(template.render(self.render_data))


    def post(self):
        schema = TareaSchema()
        errors = ValidateInput(self,schema["mensaje"],schema["titulo"],
                               ValidationObject("Tareakey").setIsRequired(True))


        if errors :
            if "Tareakey" in errors:
                self.error(402)
                return

        tareaKey = ndb.Key(urlsafe=self.Tareakey)
        tarea = tareaKey.get()

        if not tarea :
            self.error(404)
            return

        if self.user.get_id() != tarea.user:
            self.error(401)
            return

        if errors:
            wrapEntidadesSchema(self, "Tarea")
            self.render_data.update({
                "tarea" : {
                    "key" : self.Tareakey,
                    "titulo" : self.request.get("titulo",""),
                    "mensaje" : self.request.get("mensaje",""),
                }
            })
            self.render_data["errors"].update(errors)

            template = self.get_template("index.html")
            self.response.write(template.render(self.render_data))
            return


        tarea.titulo = self.titulo
        tarea.mensaje = self.mensaje

        tarea.put()
        time.sleep(1)
        self.redirect('/tareas')
