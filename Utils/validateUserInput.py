''' Validacion sencilla en el lado de servidor string/numero caracteresMaxMin/numeroMaxMin '''
''' Las funciones devuelven la CLAVE de traduccion para mostrar en el formulario '''

def ValidateInput(controller,*args):
    print (args)
    errors = {

    }
    for x in args:
        if x.required:
            if not controller.request.get(x.name) :
                errors.update({x.name : {"type": u"REQUIRED"}})
                continue

        if controller.request.get(x.name) :
            if (x.isString) :
                value = controller.request.get(x.name)

                if x.minlength :
                    if len(value) < x.minlength :
                        errors.update({x.name : {"type" : u"MINLENGTH", "params" : "{0}".format(x.minlength) }})
                        continue
                if x.maxlength :
                    if len(value) > x.maxlength :
                        errors.update({x.name : {"type" : u"MAXLENGTH","params" : "{0}".format(x.maxlength)}})
                        continue
                setattr(controller, x.name, value)
            else:
                try :
                    value = int(controller.request.get(x.name))
                except ValueError:
                    errors.update({x.name : {"type": u"NUMBER"} })
                    continue

                if x.minvalue :
                    if value < x.minvalue :
                        errors.update({x.name : {"type": u"MIN"}})
                        continue
                if x.maxvalue :
                    if value > x.maxvalue :
                        errors.update({x.name : {"type": u"MAX"}})
                        continue

        setattr(controller,x.name,value)

    print ("-")
    print (errors)
    print("-")
    return errors