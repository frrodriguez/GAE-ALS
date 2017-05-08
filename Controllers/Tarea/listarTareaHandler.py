from Controllers.BaseController.baseController import BaseHandler

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Model.Tarea import Tarea

class ListarTareaHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"ListarTarea")


    def get(self):
        wrapEntidadesSchema(self,"Tarea")


        self.render_data.update({
            "list" : Tarea.query(Tarea.user == self.user.get_id()).order(Tarea.order)
        })

        template = self.get_template( "index.html")
        self.response.write(template.render(self.render_data))
