from django.contrib import admin
from .models import BlogPost, BlogComment
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import PermissionsMixin
# Register your models here.
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'created','updated', 'TopPost')
    list_filter = ('status','author', 'created', 'updated', 'TopPost')
    search_fields = ('author', 'body', 'title', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    readonly_fields = ('updated',)
    def get_form(self, request, obj=None, **kwargs):
        form = super(BlogPostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form
@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(BlogPost, BlogPostAdmin)
