from api.models import CableModem
from api.serializers import CableModemSerializer
from api.filters import CableModemFilter
import django_filters.rest_framework
from rest_framework import generics

class CableModemList(generics.ListCreateAPIView):
    queryset = CableModem.objects.all()
    serializer_class = CableModemSerializer
    filterset_class = CableModemFilter
    def get_queryset(self):
        args = self.request.query_params.dict()
        return CableModem.objects.filter(**args)

class CableModemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CableModem.objects.all()
    serializer_class = CableModemSerializer