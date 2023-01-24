from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from testdb.models import user
from testdb.serializers import UserSerializer

@csrf_exempt
def userAPI(request, id = 0) :
    if request.method == 'GET' :
        users = user.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return JsonResponse(users_serializer.data, safe = False)
    elif request.method == 'POST' :
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data = user_data)
        if users_serializer.is_valid() :
            users_serializer.save()
            return JsonResponse("Added Successfully!", safe = False)
        return JsonResponse("Failed to add", safe = False)