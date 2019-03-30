from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Candidate, Constituency, User, Party, Eci, Voter

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Candidate)
admin.site.register(Constituency)
admin.site.register(Post)
admin.site.register(Party)
admin.site.register(Eci)
admin.site.register(Voter)
