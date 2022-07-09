from django.contrib import admin
from .models import Post

#simply adding model to the admin site
# admin.site.register(Post) 

#editing model in admin site, customisation with a custom class named PostAdmin inherits ModelAdmin
# The list_display attribute allows you to set the fields of your model that you
# want to display on the administration object list page. The @admin.register()
# decorator performs the same function as the admin.site.register() function
# that you replaced, registering the ModelAdmin class that it decorates.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')