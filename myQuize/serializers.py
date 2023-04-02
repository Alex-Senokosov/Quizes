import io
from rest_framework import serializers
from .models import Myquize
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.contrib.auth.models import User
class MyquizeSerializer (serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Myquize
        fields = ("__all__")

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']










# class MyquizeSerializer (serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Myquize.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title =validated_data.get('title',instance.title)
#         instance.content = validated_data.get('content', instance.title)
#         instance.cat_id = validated_data.get('cat_id', instance.title)
#         instance.save()
#
#         return instance


# class MyquizeModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content


# class MyquizeSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Myquize
#         fields = ("title","cat_id")
# def encode():
#     model = MyquizeModel("ang","Content: ang2")
#     model_sr= MyquizeSerializer(model)
#     print(model_sr.data,type(model_sr.data),sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO (b'{"title":"ang","content":"Content: ang2"}')
#     data = JSONParser().parse(stream)
#     serializer = MyquizeSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)