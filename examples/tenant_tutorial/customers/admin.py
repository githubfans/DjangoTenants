from django.contrib import admin

from customers.models import Client, Domain


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ('id', 'schema_name', 'name', 'description', 'created_on')

    # def get_queryset(self, request):
    #     qs = super(ClientAdmin, self).get_queryset(request)
    #     return qs
    pass


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):

    list_display = ('id', 'domain', 'is_primary', 'tenant_id')

    # def get_queryset(self, request):
    #     qs = super(DomainAdmin, self).get_queryset(request)
    #     return qs
    pass


# admin.site.register(Client, ClientAdmin)
# admin.site.register(Domain, DomainAdmin)
