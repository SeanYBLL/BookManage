from django.contrib import admin

# Register your models here.
from .models import Book,Hero

class HeroInline(admin.StackedInline):
   model = Hero
   extra = 2
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']
    search_fields = ['title']
    list_filter = ['title']
    fieldsets = [('基础信息',{'fields':['title']}),
                 ('详细信息',{'fields':['pub_date']}),]
    inlines = [HeroInline]

class HeroAdmin(admin.ModelAdmin):
    list_display = ['id','name','content', 'sex']
    search_fields = ['name']
    list_filter = ['name']
    list_per_page = 2
    fieldsets = [('基础信息',{'fields':['name', 'gender']}),
                 ('详细信息',{'fields':['content']}),]

admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)
