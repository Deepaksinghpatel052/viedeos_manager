from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import VsHomePageSettings
# Register your models here.
class VsHomePageSettingsAdmin(ImportExportModelAdmin):
    list_display = ('Video_Of_The_Day','Session_2_Title','Session_3_box_1_Title','Session_3_box_2_Title','Session_3_box_3_Title','Updated_date')
admin.site.register(VsHomePageSettings,VsHomePageSettingsAdmin)
