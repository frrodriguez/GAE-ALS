from google.appengine.api import users

from Model.User import User
from Model.UserStoredData import UserStoredData

import time

def wrapUsuarioLogeado(controller):
    ''' Establece el usuario logeado actualmente '''
    user = users.get_current_user()

    if user:
        dataUser = UserStoredData.query(UserStoredData.user == user.user_id())
        if dataUser.count() > 0:
            controller.user = User(user, users.is_current_user_admin(), dataUser.fetch()[0].idioma)
        else:
            dataUser = UserStoredData(user=user.user_id(),idioma="es")
            dataUser.put()
            time.sleep(1)
            controller.user = User(user, users.is_current_user_admin(), idioma="es")

        if controller.render_data :
            controller.render_data.update({
                "currentUser" : controller.user
            })
    else:
        controller.user = None