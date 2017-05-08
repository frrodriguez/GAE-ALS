from google.appengine.api import users
from Model.User import User

def wrapUsuarioLogeado(controller):
    ''' Establece el usuario logeado actualmente '''
    user = users.get_current_user()
    print("<1>")
    print (user.user_id())
    if user:
        controller.user = User(user, users.is_current_user_admin())
        print("<2>")
        print(controller.user.get_id())
        if controller.render_data :
            controller.render_data.update({
                "currentUser" : controller.user
            })
    else:
        controller.user = None