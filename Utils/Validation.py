
class ValidationObject:
    def __init__(self, name, isString = True):
        self.name = name
        self.isString = isString
        self.required = False
        self.minlength = None
        self.maxlength = None
        self.minvalue = None
        self.maxvalue = None

    def setIsRequired(self,boolean):
        self.required = boolean
        return self

    def setMinLength(self,value):
        self.minlength = value
        return self

    def setMinValue(self,value):
        self.minvalue = value
        return self

    def setMaxLength(self,value):
        self.maxlength = value
        return self

    def setMaxValue(self,value):
        self.maxvalue = value
        return self

    def __str__(self):
        ''' Se contruyen los atributos de validacion html5'''
        return "{0} {1} {2} {3} {4}".format("required" if self.required else "",
                                            "minlength={0}".format(self.minlength) if self.minlength else "",
                                            "min={0}".format(self.minvalue) if self.minvalue else "",
                                            "maxlength={0}".format(self.maxlength) if self.maxlength else "",
                                            "max={0}".format(self.maxvalue) if self.maxvalue else "",)