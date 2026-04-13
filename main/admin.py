from django.contrib import admin
from django.utils.html import format_html
from .models import *
admin.site.register(Category)
admin.site.register(Tag)

class ContextInline(admin.StackedInline):
    model = Context
    extra = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_tag',  'author', 'views', 'read_time', 'puplished', 'important', 'category', 'created_at')
    def cover_tag(self,obj):
        if obj.cover:
            return format_html(
                '<img src="{}" style="height: 45px; widht:80px; object-fit: cover;" />',
                obj.cover.url
            )
        return "-"
    list_filter = ('category', 'puplished', 'important')
    date_hierarchy = 'created_at'
    inlines= (ContextInline, CommentInline)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'article')


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo_tag', 'author', 'views', 'published', 'created_at')


    def photo_tag(self,obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="height: 45px; widht: 80px; object-fit: cover;" />',
            )
        return "-"

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'phone_number', 'subject', 'created_at', 'seen')
