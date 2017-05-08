
from Controllers.BaseController.baseController import BaseHandler

class InicioHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"Inicio")


    def get(self):

        self.render_data["name"] = "prueba";

        print ("2-------------------------")
        print (self.render_data)
        template = self.get_template( "inicio.html")
        self.response.write(template.render(self.render_data))
