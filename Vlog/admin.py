from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VlogPost, VlogComment
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import PermissionsMixin
# Register your models here.
class VlogPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'created', 'top_post')
    list_filter = ('status','author', 'created', 'updated', 'top_post')
    search_fields = ('author', 'body', 'title', 'created')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    readonly_fields = ('updated',)
    def get_form(self, request, obj=None, **kwargs):
        form = super(VlogPostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form
@admin.register(VlogComment)
class VlogCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(VlogPost,VlogPostAdmin)
