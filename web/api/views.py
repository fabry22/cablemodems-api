from api.models import CableModem
from api.serializers import CableModemSerializer
from rest_framework import generics

class CableModemList(generics.ListCreateAPIView):
    queryset = CableModem.objects.all()
    serializer_class = CableModemSerializer


class CableModemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CableModem.objects.all()
    serializer_class = CableModemSerializer