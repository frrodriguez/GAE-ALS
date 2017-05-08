

from Utils.I18n.i18n import traductionCreator


def wrapi18n(controller):
    if controller.render_data :
        controller.render_data.update({
            "t": traductionCreator("es"),  # Variable t almacena la funcion que se emplea para la traduccion
        })