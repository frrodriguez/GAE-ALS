from Controllers.BaseController.baseController import BaseHandler


import time

from Utils.validateUserInput import ValidateInput
from Utils.Validation import ValidationObject

from google.appengine.ext import ndb

class MoverTareaTareaHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"MoverTarea")

    def post(self):
        errors = ValidateInput(self,
                               ValidationObject("key").setIsRequired(True),
                               ValidationObject("userTarea").setIsRequired(True),
                               ValidationObject("estado",False).setIsRequired(True).setMinValue(1).setMaxValue(2),
                               ValidationObject("order", False).setIsRequired(True).setMinValue(0))

        if errors:
            print (errors)
            self.error(400)
            return

        if self.user.get_id() != self.userTarea:
            self.error(401)
            return

        tareaKey = ndb.Key(urlsafe=self.key)
        tarea = tareaKey.get()
        tarea.order = self.order
        tarea.estado = self.estado

        tarea.put()
        time.sleep(1)
        self.response.set_status(200)
