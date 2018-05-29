from django.contrib import admin
from news.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","updated", "date"]
    # list_editable = ["title"]
    list_filter = ["updated", "date"]
    search_fields = ["title", "body"]
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
