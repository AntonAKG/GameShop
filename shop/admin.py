from django.contrib import admin

from .models import Game, GalleryGame


class GalleryInline(admin.TabularInline):
    model = GalleryGame


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
