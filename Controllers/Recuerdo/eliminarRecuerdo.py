from Controllers.BaseController.baseController import BaseHandler

import time

from Utils.Wrappers.entityWrapper import wrapEntidadesSchema
from Utils.validateUserInput import ValidateInput
from Utils.Validation import ValidationObject

from Model.Tarea import Tarea
from Model.Tarea import TareaSchema

from google.appengine.ext import ndb

class EliminarRecuerdoHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"EliminarRecuerdo")
        print ("INIT")
        print (self.request)





    def post(self):
        schema = TareaSchema()
        errors = ValidateInput(self,
                               ValidationObject("Recuerdokey").setIsRequired(True))


        if errors :
            if "Recuerdokey" in errors:
                self.response.set_status(402,"Bad request")
                return

        recuerdoKey = ndb.Key(urlsafe=self.Recuerdokey)
        recuerdo = recuerdoKey.get()

        if not recuerdo :
            self.response.set_status(404,"Not Found")
            return

        if self.user.get_id() != recuerdo.user:
            self.response.set_status(401,"Unauthorized")
            return

        print("RECUERDO ENCONTRADO")
        print(recuerdo.mensaje)
        recuerdoKey.delete()
        time.sleep(1)

        self.redirect('/recuerdos')
