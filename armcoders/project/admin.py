from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","img")
    list_editable = ("name","img")

admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("id","name","img","img_1","category","about","about_detail","link","view")
    list_editable = ("name","img","img_1","category","about","about_detail","link","view")
    search_fields = ("id","name","category")

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","name","comment")
    search_fields = ("id","name","comment")

admin.site.register(Comment,CommentAdmin)