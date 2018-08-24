from django.conf.urls import include, url
# from django.urls import path
from tenant_tutorial.views import HomeView
from django.contrib import admin
from rest_framework import routers
from barang import views

router = routers.DefaultRouter()
# router.register(r'postcategory', views.PostCategoryViewSet)
router.register(r'post', views.PostViewSet)

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^barang/', include(router.urls)),
    url(r'^barang-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
