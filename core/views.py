from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import AddressSerializer
from .utils import get_geocode_response

class AddressDetails(APIView):
    def post(self, request, format=None):
        ser = AddressSerializer(data=request.data)
        if ser.is_valid():
            output_format = ser.data['output_format']
            address = ser.data['address']
            
            geocode_response = get_geocode_response(address)
            if output_format == 'xml':
                return Response(geocode_response,)
            elif output_format == 'json':
                return JsonResponse(geocode_response)
            else:
                data = {'error': 'Invalid output format. Available options are "json" and "xml" '}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            data = {'error': ser.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
