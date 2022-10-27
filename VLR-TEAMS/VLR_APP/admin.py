from django.contrib import admin
from django.db import models
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(User)
admin.site.register(Team)

admin.site.register(Player)
admin.site.register(Coache)
admin.site.register(Anuncio)
admin.site.register(Directivo)


