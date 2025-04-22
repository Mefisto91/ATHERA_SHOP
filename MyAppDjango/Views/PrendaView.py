from rest_framework import viewsets
from ..Serializers.PrendaSerializer import PrendaS
from ..Models.PrendaModel  import PrendaM

class PrendaV(viewsets.ModelViewSet):
    queryset = PrendaM.objects.all()
    serializer_class = PrendaS





