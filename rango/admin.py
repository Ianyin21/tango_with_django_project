<<<<<<< HEAD
from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
=======
from django.contrib import admin

# Register your models here.
>>>>>>> ddb9f11ee539b3992753f11402017d470cdc5e89
