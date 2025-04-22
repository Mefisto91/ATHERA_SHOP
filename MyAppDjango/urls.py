from django.urls import path, include
from rest_framework import routers
from MyAppDjango.Views import PrendaView 

router = routers.DefaultRouter()
router.register(r'Prenda', PrendaView.PrendaV)

urlpatterns = [
    path('', include(router.urls))
]

