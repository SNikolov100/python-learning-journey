from django.contrib import admin
from .models import Note

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['priority']
    
