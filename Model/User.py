
class User:
    def __init__(self,AppEngineUser,isAdmin):
        self.APU = AppEngineUser
        self.isAdmin = isAdmin;

    def get_nickname(self):
        return self.APU.nickname()

    def get_id(self):
        return self.APU.user_id()

    def get_email(self):
        return self.APU.email()

    def isAdmin(self):
        return self.isAdmin

    def __str__(self):
        if (self.APU) :
            return "{0}, {1}".format(self.get_nickname(),self.get_email())
        else :
            return "NONE USER"