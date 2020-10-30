from api.models import CableModem
from api.serializers import CableModemSerializer, CableModemModelSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from decouple import config
import os, json
from rest_framework.response import Response
import logging

def path_resolver(relative_path):
    script_dir = os.path.dirname(__file__) 
    return os.path.join(script_dir, relative_path)

def model_append(data):
    reference_route = path_resolver(config('JSON_REFERENCE_MODELS'))
    tmp_route = reference_route+".tmp"
    try:
        out_data = None
        with open(reference_route, "r+") as ref_file:
            out_data = json.load(ref_file)
            out_data[config('CM_MODELS')].append(data)
        with open(tmp_route, "w+") as out_file:
            json.dump(out_data, out_file, indent=config('IDENT', cast=int))
    except:
        logging.error(config('ERR_WR_JSON_MODEL_MSG'))
        return False
    else:
        os.remove(reference_route)
        os.rename(tmp_route, reference_route)
        return True

class CableModemList(generics.ListCreateAPIView):
    queryset = CableModem.objects.all()
    serializer_class = CableModemSerializer
    def get_queryset(self):
        args = self.request.query_params.dict()
        return CableModem.objects.filter(**args)

class CableModemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CableModem.objects.all()
    serializer_class = CableModemSerializer

class CableModemModelsList(APIView):
    def get(self, request, format=None):
        req_args = request.query_params.dict()
        vendor = config('VENDOR')
        name = config('NAME')
        soft = config('SOFT')
        if vendor in req_args:
            reference_route = path_resolver(config('JSON_REFERENCE_MODELS'))
            name_args = []
            soft_args = []
            vendor_name = req_args[vendor]
            with open(reference_route, 'r') as json_ref:
                models = json.load(json_ref)[config('CM_MODELS')]
                for model in models:
                    if (vendor_name == model[vendor]):
                        name_args.append(model[name])
                        soft_args.append(model[soft])
            if not name_args:
                return Response(config('ERR_REQ_WO_VEND_MSG').format(vendor_name), status=status.HTTP_404_NOT_FOUND)
            else:
                include = { config('REG_VENDOR') : vendor_name }
                exclude_sw = {
                    config('REG_SWV')+config('IN') : soft_args
                }
                exclude_model = {
                    config('REG_MODEL')+config('IN') : name_args
                }
                cms = CableModem.objects.filter(**include).exclude(**exclude_sw).exclude(**exclude_model)
                serializer = CableModemSerializer(cms, many=True)
                return Response(serializer.data)
        else:
            return Response(config('ERR_REQ_WO_VEND_MSG'), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = CableModemModelSerializer(data=request.data)
        if serializer.is_valid():
            success = model_append(serializer.data)
            if success:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(config('ERR_WR_JSON_MODEL_MSG'), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)