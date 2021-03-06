from django.contrib import admin
from .models import Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Recipe, RecipeAdmin)