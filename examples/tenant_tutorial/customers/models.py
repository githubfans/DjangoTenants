from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created_on = models.DateField(null=True, auto_now_add=True)

    auto_create_schema = True
    auto_drop_schema = True


class Domain(DomainMixin):
    # domain = models.CharField(max_length=100)
    # is_primary = models.BooleanField(default=True)
    # created_on = models.DateField(null=True, editable=True, auto_now_add=True)
    # tenant = models.ForeignKey(Client, null=False, editable=True, default='', on_delete=False)
    pass
