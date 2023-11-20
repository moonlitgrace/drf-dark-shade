from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import serializers

class TestSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=500)
	email = serializers.EmailField()

class TestAPIView(CreateAPIView):
	serializer_class = TestSerializer