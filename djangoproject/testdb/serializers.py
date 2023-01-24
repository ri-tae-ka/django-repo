from rest_framework import serializers
from testdb.models import user

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = user
        fields = ('id', 'name', 'age')