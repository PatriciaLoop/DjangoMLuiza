from api.serializers import ClientSerializer, ProductSerializer
from rest_framework import viewsets
from api.models import Client, Product
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all().order_by('id')
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]