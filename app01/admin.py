from django.contrib import admin
from app01 import models;
# Register your models here.


def make_forbidden(modelAdmin,request,queryset):
    print('---->',request,queryset)
    queryset.update(status='forbindden')
    make_forbidden.short_description = "Set to forbidden"


class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','publisher','publication_date','status')
    search_fields = ('title','publisher__name')
    list_filter = ('publisher__name','publication_date')
    list_editable = ('title','publication_date')
    list_per_page = 10
    # list_select_related = ('publisher',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
    actions = [make_forbidden,]

admin.site.register(models.Author)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Publisher)