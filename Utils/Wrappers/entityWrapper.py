
import importlib

def wrapEntidadesSchema(controller,*entidades):
    ''' Metodo que anade dinamicamente las entidades del modelo necesarias al controlador. La entidad y el nombre del
    fichero donde se encuentran debe ser el mismo (+Schema)'''
    if controller.render_data :
        for entidad in entidades:
            controller.render_data.update({
                "Schema{0}".format(entidad) : getattr(importlib.import_module("Model.{0}".format(entidad)), "{0}Schema".format(entidad))(),  # Se recorre el directorio de model importando las entidades necesarias
            })