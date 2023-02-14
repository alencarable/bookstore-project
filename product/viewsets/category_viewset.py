from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    
    def get_queryset(self):     #it is possible to instance as a method
        return Category.objects.all()  