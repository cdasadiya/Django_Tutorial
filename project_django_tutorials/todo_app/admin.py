from django.contrib import admin
from .models import Create_Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    icon_name = "person"

    list_display = ('task', 'is_completed', 'created_at','updated_at',)
    search_fields = ('task',)
    list_filter=('is_completed',)

admin.site.register(Create_Task,TaskAdmin)
