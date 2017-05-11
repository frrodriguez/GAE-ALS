

from Utils.I18n.i18n import traductionCreator


def wrapi18n(controller):
    idioma = "es"
    if controller.user:
        idioma = controller.user.idioma
        print("IDIOMA USUARIO")
        print(idioma)

    if controller.render_data :
        controller.render_data.update({
            "t": traductionCreator(idioma),  # Variable t almacena la funcion que se emplea para la traduccion
        })