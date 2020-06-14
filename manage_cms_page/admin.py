from django.contrib import admin
from .models import VsCmsPage
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class VsCmsPageAdmin(ImportExportModelAdmin,SummernoteModelAdmin):
    summernote_fields = ('Page_content',)
    list_display = ('Title','keywork','Background_Image','Description')
admin.site.register(VsCmsPage,VsCmsPageAdmin)
