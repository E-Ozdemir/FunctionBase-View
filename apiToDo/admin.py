from django.contrib import admin
from .models import ToDo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "task",
        "description",
        "priority",
        "done",
        "updateDate",
        # "createDate",
    ]
    
    
    
    
    
admin.site.register(ToDo,TodoAdmin)
