from django.contrib import admin
from .models import comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'article', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'article']
admin.site.register(comment,CommentAdmin)
# Register your models here.
