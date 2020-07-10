from django.contrib import admin
from .models import Category, Blog, MemberInfo

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(MemberInfo)