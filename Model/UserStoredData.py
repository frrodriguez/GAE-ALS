
from google.appengine.ext import ndb

class UserStoredData(ndb.Model):
    user = ndb.StringProperty(required=True)
    idioma = ndb.StringProperty(required=True)
