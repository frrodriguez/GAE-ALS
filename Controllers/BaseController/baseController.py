
import webapp2

from configJinja import JINJA_ENVIRONMENT

from Utils.Wrappers.i18nWrapper import wrapi18n
from Utils.Wrappers.userWrapper import wrapUsuarioLogeado

from google.appengine.api import users


class BaseHandler(webapp2.RequestHandler):

    def __init__(self, request, response, controllerName):
        # Set self.request, self.response and self.app.
        self.initialize(request, response)

        ''' Se establece la funcion de traduccion como payload del objeto que recibiran las plantillas
        y valores por defecto para otras variables'''
        self.render_data = {
            "login_url" : lambda url : users.create_login_url(url),  # Funciones para crear login y logout en las plantillas
            "logout_url" : lambda url : users.create_login_url(url),  # Funciones para crear login y logout en las plantillas
            "globalError" : None,  # Mensaje de error
            "errors" : { },  # Mensaje de error
            "currentUser" : None
        }


        wrapUsuarioLogeado(self) # Establece el usuario logueado
        wrapi18n(self) # Funcion de traduccion

        print (controllerName)

        ''' Nombre del controlador. IMPORTANTE, el nombre se usa para buscar las plantillas'''
        self.controllerName = controllerName

    ''' Metodo que devuelve una platilla dado su nombre ( con extension ) '''
    def get_template(self,templateName):
        return JINJA_ENVIRONMENT.get_template("{0}/{1}".format(self.controllerName,templateName))

    def is_user_loged(self):
        return True if self.user else False