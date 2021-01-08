from django.contrib import admin
from .models import ReviewPost, ReviewComment, Category
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import PermissionsMixin
# Register your models here.
@admin.register(ReviewPost)
class ReviewPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'created','updated', 'TopPost', 'overall')
    list_filter = ('status','author', 'created', 'updated', 'TopPost', 'overall')
    search_fields = ('author', 'body', 'title', 'created')
    prepopulated_fields = {'slug': ('title',),}
    summernote_fields = ('body',)
    readonly_fields = ('updated','overall')
    def get_form(self, request, obj=None, **kwargs):
        form = super(ReviewPostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form

@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category',)
    list_filter=('category',)
