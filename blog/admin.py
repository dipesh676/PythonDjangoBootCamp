from django.contrib import admin

# Register your models here.
from .models import Category,BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'publish_date', 'category', 'publish', 'created', 'updated']
	list_filter = ['author','updated', 'publish', 'category']
	list_editable = ['title', 'publish']
	search_fields = ['title', 'content']
	list_per_page = 5

admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)