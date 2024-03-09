from django.contrib import admin

# Register your models here.
from .models import Game, Character, Tag, User  # Update with actual model names

admin.site.register(Game)
admin.site.register(Character)
admin.site.register(Tag)
#admin.site.register(User)
