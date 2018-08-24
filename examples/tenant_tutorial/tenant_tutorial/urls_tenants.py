from customers.views import TenantView
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from barang import views

router = routers.DefaultRouter()
# router.register(r'postcategory', views.PostCategoryViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', TenantView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^barang/', include(router.urls)),
    url(r'^barang-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
