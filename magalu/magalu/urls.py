from django.contrib import admin
from api.views import ClientViewSet, ProductViewSet
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register('clients', ClientViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include(router.urls) )
]