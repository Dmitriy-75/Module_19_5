from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(News)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','content','date',)
    list_filter = ('title','date',)
    search_fields = ('title',)
    list_per_page = 10


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','cost','size',)
    list_filter = ('size','cost',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name','balance','age',)
    list_filter = ('balance','age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)