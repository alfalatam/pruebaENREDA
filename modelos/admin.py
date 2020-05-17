from django.contrib import admin
from .models import User, note
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'Nombre', 'Email')


admin.site.register(User, UserAdmin)


class NoteAdmin(admin.ModelAdmin):

    list_display = ('ID', 'Note', 'Type', 'task', 'Date',
                    'EndDate', 'Adjunto')

    fields = ('Date', 'EndDate', 'Note', 'Adjunto',
              'user', 'Type', 'task', 'tags')

    readonly_fields = ('Date',)


admin.site.register(note, NoteAdmin)
