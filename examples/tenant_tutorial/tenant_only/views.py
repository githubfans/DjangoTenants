from .models import TableOne, TableTwo
from rest_framework import viewsets


class TableOneViewSet(viewsets.ModelViewSet):
    queryset = TableOne.objects.all()

    def get_queryset(self):
        if is_authenticated(self.request.user):
            return TableOne.objects.all()
        else:
            pass


class TableTwoViewSet(viewsets.ModelViewSet):
    queryset = TableTwo.objects.all()

    def get_queryset(self):
        if is_authenticated(self.request.user):
            return TableTwo.objects.all()
        else:
            pass


def is_authenticated(user):
    '''

    Django 2.0: 'bool' object is not callable is_authenticated #218
    https://github.com/juanifioren/django-oidc-provider/issues/218#issuecomment-349220098

    '''
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated
