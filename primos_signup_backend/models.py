from django.db.models import *

class Primo(Model):
    rol = CharField(primary_key=True, max_length=11)
    mail = CharField(unique=True, max_length=100)
    
    name = CharField(max_length=100)
    nick = CharField(max_length=100)

    bussy_schedule = CharField(max_length=100)
    desire_schedule = CharField(max_length=100)
    
    new = BooleanField(default=False)
