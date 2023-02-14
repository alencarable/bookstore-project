#from rest_framework import status
#from rest_framework.mixins import CreateModelMixin
#from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer  #a viewset needs a serializer
    queryset = Order.objects.all()  #query default de listagem