from rest_framework import serializers
from .models import CustomUser, DataModel

# Serializer for CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'country', 'role']

# Serializer for DataModel (Added)
class DataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = ['id', 'user', 'data_field', 'created_at']
