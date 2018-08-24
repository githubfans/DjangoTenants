from django.contrib.auth.models import User
from django.db.utils import DatabaseError
from django.views.generic import FormView
from customers.forms import GenerateUsersForm
from customers.models import Client
from random import choice
import random


class TenantView(FormView):
    form_class = GenerateUsersForm
    template_name = "index_tenant.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(TenantView, self).get_context_data(**kwargs)
        context['tenants_list'] = Client.objects.all()
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        User.objects.all().delete()  # clean current users

        # generate five random users
        USERS_TO_GENERATE = random.randint(5, 20)
        first_names = ["Irvan", "Bino", "Erwin", "Khadafi", "Salmaa", "Muharram",
                       "igun", "ayix", "Fajar", "Yantoo"]
        last_names = ["Smith", "Shith", "Brown", "Brownies", "Lee", "Leetakkan",
                      "Wilson", "Wilyoung", "Martin", "Martan", "Patel", "6atel",
                      "Taylor", "Paylor", "Wong", "Wonge Dewe", "Campbell",
                      "Sampbell", "Brillians", "Williams"]

        while User.objects.count() != USERS_TO_GENERATE:
            first_name = choice(first_names)
            last_name = choice(last_names)
            try:
                user = User(username=(first_name + last_name).lower(),
                            email="%s@%s.com" % (first_name, last_name),
                            first_name=first_name,
                            last_name=last_name)
                user.save()
            except DatabaseError:
                pass

        return super(TenantView, self).form_valid(form)
