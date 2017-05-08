from Controllers.BaseController.baseController import BaseHandler

import time

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Utils.validateUserInput import ValidateInput

from Model.Tarea import Tarea
from Model.Tarea import TareaSchema

class CrearTareaHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"CrearTarea")
        print ("INIT")
        print (self.request)


    def get(self):
        print (self.render_data)
        wrapEntidadesSchema(self,"Tarea")


        self.render_data.update({
            "tarea" : Tarea() #  Valor por defecto que se mostrara en el formulario
        })

        template = self.get_template( "index.html")
        self.response.write(template.render(self.render_data))


    def post(self):
        schema = TareaSchema()
        errors = ValidateInput(self, schema["mensaje"], schema["titulo"])

        if errors :
            wrapEntidadesSchema(self, "Tarea")
            self.render_data.update({
                "tarea" : {
                    "titulo" : self.request.get("titulo",""),
                    "mensaje" : self.request.get("mensaje",""),
                }
            })
            self.render_data["errors"].update(errors)

            template = self.get_template("index.html")
            self.response.write(template.render(self.render_data))
            return

        tareas = Tarea.query().order(Tarea.order);
        nuevaTarea = Tarea(titulo=self.titulo,
                           mensaje=self.mensaje,
                           order=(tareas.count()+1),
                           estado=False,
                           user=self.user.get_id())
        nuevaTarea.put()
        time.sleep(1)
        self.redirect('/tareas',True)
