from django.contrib import admin
from .models import Category, Post, Comment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields= ["name"]
    



class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


