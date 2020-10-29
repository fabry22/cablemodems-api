import django_filters
from api.models import CableModem

class CableModemFilter(django_filters.FilterSet):
    class Meta:
        model = CableModem
        #Entiendo que este campo no posee una gran importancia, en caso de no ser así puede excluirse cualquier otro
        exclude = []