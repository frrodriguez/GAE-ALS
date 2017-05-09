from google.appengine.api import users
from Model.User import User

def wrapUsuarioLogeado(controller):
    ''' Establece el usuario logeado actualmente '''
    user = users.get_current_user()
    if user:
        controller.user = User(user, users.is_current_user_admin())
        if controller.render_data :
            controller.render_data.update({
                "currentUser" : controller.user
            })
    else:
        controller.user = None