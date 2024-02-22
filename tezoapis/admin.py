from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee

class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ('empid', 'firstname', 'lastname', 'DOB', 'emailid', 'mobile', 'joining', 'location', 'jobtitle', 'Department', 'AssignManager', 'AssignProject', 'profilepath', 'status')
    list_filter = ('location', 'jobtitle', 'Department', 'status')
    search_fields = ('empid', 'firstname', 'lastname', 'emailid', 'mobile')

admin.site.register(Employee, EmployeeAdmin)
