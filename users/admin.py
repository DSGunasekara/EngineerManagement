from django.contrib import admin
from .models import Profile

admin.site.site_header = "Field Engineer Management Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to Field Engineer Management Admin Area"

admin.site.register(Profile)
