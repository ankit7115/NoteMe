from rest_framework.serializers import ModelSerializer
from .models import Todo

class todoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'