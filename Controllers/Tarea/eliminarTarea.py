from Controllers.BaseController.baseController import BaseHandler

import time

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Utils.validateUserInput import ValidateInput
from Utils.Validation import ValidationObject

from Model.Tarea import Tarea
from Model.Tarea import TareaSchema

from google.appengine.ext import ndb

class EliminarTareaHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"EliminarTarea")
        print ("INIT")
        print (self.request)





    def post(self):
        schema = TareaSchema()
        errors = ValidateInput(self,
                               ValidationObject("Tareakey").setIsRequired(True))


        if errors :
            if "Tareakey" in errors:
                self.response.set_status(402,"Bad request")
                return

        tareaKey = ndb.Key(urlsafe=self.Tareakey)
        tarea = tareaKey.get()

        if not tarea :
            self.response.set_status(404,"Not Found")
            return

        if self.user.get_id() != tarea.user:
            self.response.set_status(401,"Unauthorized")
            return


        tareaKey.delete()
        time.sleep(1)
        self.redirect('/tareas',True)
