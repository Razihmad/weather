from django.contrib import admin

from app.models import Details

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display=('username','email','city','time')
    
    
