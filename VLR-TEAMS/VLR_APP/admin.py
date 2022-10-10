from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.
admin.site.register(team)
admin.site.register(client)
admin.site.register(player)
admin.site.register(coache)
admin.site.register(anuncio)
admin.site.register(directivo)


