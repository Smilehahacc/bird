from django.contrib import admin
from .models import User,Img

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_password','user_power']
class ImgAdmin(admin.ModelAdmin):
    list_display = ['img_id', 'img_url', 'img_sign','img_result']

admin.site.register(User,UserAdmin)
admin.site.register(Img,ImgAdmin)
