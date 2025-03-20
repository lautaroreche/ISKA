from django.contrib import admin
from iska_app.models import Carousel, Service, Faq, Team, Post
from django.contrib.sessions.models import Session


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_button', 'image')
    list_filter = ('title', 'text_button')
    search_fields = ('title', 'text_button')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text_button', 'image', 'key_words')
    list_filter = ('title', 'description', 'text_button', 'key_words')
    search_fields = ('title', 'description', 'text_button', 'key_words')


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_filter = ('question', 'answer')
    search_fields = ('question', 'answer')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'image')
    list_filter = ('full_name', 'position')
    search_fields = ('full_name', 'position')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Session)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Post, PostAdmin)
