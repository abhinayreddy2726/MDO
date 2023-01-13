from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
class ItemViewSet(viewsets.ModelViewSet):
 queryset = Item.objects.all()
 serializer_class = ItemSerializer
 def get_queryset(self):
    category = self.request.query_params.get('category', None)
    if category is not None:
        return Item.objects.filter(category=category)
    return Item.objects.all()