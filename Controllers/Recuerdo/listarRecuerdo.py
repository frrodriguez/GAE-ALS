from Controllers.BaseController.baseController import BaseHandler

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Model.Recuerdo import Recuerdo

class ListarRecuerdoHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"ListarRecuerdo")


    def get(self):

        self.render_data.update({
            "list" : Recuerdo.query(Recuerdo.user == self.user.get_id()).order(Recuerdo.fecha)
        })

        template = self.get_template( "index.html")
        self.response.write(template.render(self.render_data))
