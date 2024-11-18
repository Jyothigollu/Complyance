from rest_framework import viewsets
from .models import CustomUser, DataModel
from .serializers import CustomUserSerializer, DataModelSerializer

# ViewSet for CustomUser
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# ViewSet for DataModel
class DataModelViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = DataModelSerializer
