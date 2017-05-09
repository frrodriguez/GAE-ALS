from Controllers.BaseController.baseController import BaseHandler


import time

from Utils.validateUserInput import ValidateInput
from Utils.Validation import ValidationObject

from Utils.I18n.i18n import getLenguajesDisponibles

from Model.UserStoredData import UserStoredData
from google.appengine.ext import ndb

class CambiarIdiomaHandler(BaseHandler):

    def __init__(self,req,res):
        BaseHandler.__init__(self,req,res,"CambiarIdioma")

    def post(self):
        errors = ValidateInput(self,
                               ValidationObject("idioma").setIsRequired(True))

        if errors:
            print (errors)
            self.error(400)
            return
        if "{0}.py".format(self.idioma) not in getLenguajesDisponibles():
            print("{0}.py".format(self.idioma))
            print(getLenguajesDisponibles())
            print ("Idioma incorrecto")
            self.error(400)
            return

        dataUser = UserStoredData.query(UserStoredData.user == self.user.get_id())
        if dataUser.count() > 0:
            print("IDioma cambiado")
            dataUser.fetch(1)[0].idioma = self.idioma
            dataUser.fetch(1)[0].put()
            time.sleep(1)

        self.redirect('/',True)
