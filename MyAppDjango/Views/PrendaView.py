from ..Serializers.PrendaSerializer import PrendaS
from ..Models.PrendaModel  import PrendaM
from rest_framework import viewsets

class PrendaV(viewsets.ModelViewSet):
    queryset = PrendaM.objects.all()
    serializer_class = PrendaS





