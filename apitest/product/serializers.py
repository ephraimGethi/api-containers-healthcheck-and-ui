from rest_framework.serializers import ModelSerializer
from .models import computer,Rooms
from rest_framework import serializers


class computerSerializer(ModelSerializer):
    avatar = serializers.ImageField(write_only = True)
    image = serializers.SerializerMethodField()
    class Meta:
        model = computer
        fields =['name','avatar','image','description']

    def get_image(self,obj):
        return obj.image_url()
    

class RoomSerializer(ModelSerializer):
    updated_at = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    class Meta:
        model= Rooms
        fields = ['name','description','updated_at','created_at']