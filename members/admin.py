from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display=("fname","lname","email")
    prepopulated_fields={"slug":("fname","lname")}
admin.site.register(Member,MemberAdmin)
