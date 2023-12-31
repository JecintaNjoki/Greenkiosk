from django.contrib import admin

# Register your models here.
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    list_filter = ('name','category')

admin.site.register(Category, CategoryAdmin)