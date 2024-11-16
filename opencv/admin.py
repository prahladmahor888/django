from django.contrib import admin
from opencv.models import createuser, UploadImage, cardEvent
class opencvAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'password')

class uploadImage(admin.ModelAdmin):
    list_display = ('userid','first_name','last_name', 'image',)

class CardEvent(admin.ModelAdmin):
    list_display = ('eventText', 'eventImage')


admin.site.register(cardEvent, CardEvent)
admin.site.register(createuser, opencvAdmin)
admin.site.register(UploadImage, uploadImage)

# Register your models here.
