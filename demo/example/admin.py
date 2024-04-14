from django.contrib import admin

# Register your models here.
from . import models

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt',)

admin.site.register(models.Note, NoteAdmin)
admin.site.register(models.Image, ImageAdmin)