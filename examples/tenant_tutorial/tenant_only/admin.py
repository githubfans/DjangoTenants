from django.contrib import admin

from tenant_only.models import TableOne, TableTwo


# @admin.register(TableOne)
class TableOneAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

    def get_queryset(self, request):
        qs = super(TableOneAdmin, self).get_queryset(request)
        return qs
    # pass


# @admin.register(TableTwo)
class TableTwoAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'table_one')

    def get_queryset(self, request):
        qs = super(TableTwoAdmin, self).get_queryset(request)
        return qs
    # pass


admin.site.register(TableOne, TableOneAdmin)
admin.site.register(TableTwo, TableTwoAdmin)
