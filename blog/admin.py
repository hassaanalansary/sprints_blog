from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ['title', 'author__username']
    list_filter = ['title', 'author', 'created_at']
    


admin.site.register(Post, PostAdmin)
