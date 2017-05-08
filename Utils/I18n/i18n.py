
defaultLang = "es"
arrayLang = []

import importlib
from os import listdir



def traductionCreator(lang):
    ''' Crea la funcion que se encarga de realizar las traducciones en la templates comprobando el
    directorio de Locales '''

    ''' Se comprueba dinamicamente que existe el fichero de traducciones del lenguaje especificado'''
    if ( "{0}.py".format(lang) == traductionFiles for traductionFiles in listdir("Utils/I18n/Locales")):
        defaultLang = lang

    ''' Se importa el correspondiente lenguaje. Debe contener un array translations con las traducciones'''
    arrayLang = importlib.import_module("Utils.I18n.Locales."+defaultLang).translations

    return lambda s, *args : replace(arrayLang[s], *args) if s in arrayLang else s




def replace(value, *args):
    ''' Funcion auxiliar que substituye los valores auxiliares de traduccion
        Ej: ("Bienvenido: %2, %1", "Fran", "Rojas") => Bienvenido: Rojas, Fran '''

    for x in range(0, len(args)):
        value = value.replace("%{0}".format(x+1), args[x] if args[x] else "UNDEFINED_VALUE")

    return value

