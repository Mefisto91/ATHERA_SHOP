from django.urls import path, include
from rest_framework import routers
from MyAppDjango.Views.PrendaView import PrendaV

router = routers.DefaultRouter()
router.register(r'Prenda', PrendaV)

urlpatterns = [
    path('', include(router.urls))
]

