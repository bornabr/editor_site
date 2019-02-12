from django.contrib import admin
from .models import Post


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_share', 'date_posted')
    fields = ('image_tag', 'name', 'image', 'is_share', 'date_posted')
    readonly_fields = ('image_tag',)


admin.site.register(Post, PostAdmin)
