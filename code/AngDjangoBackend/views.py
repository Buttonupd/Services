from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    permission_classes = (IsAuthenticated)

    permission_classes = (IsAdminOrReadOnly,)
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)

        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data = tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} tut deleted'.format(count[0])}, status= status.HTTP_204_NO_CONTENT)



@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    permission_classes = (IsAuthenticated)
    try:
        tutorial = Tutorial.objects.get(pk=pk)

    except Tutorial.DoesNotExist:
        return JsonResponse({'message':'Tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message':'Tutorial deleted'}, status = status.HTTP_204_NO_CONTENT)
@csrf_exempt
@api_view(['GET'])
def tutorial_list_published(request):
    permission_classes = (IsAuthenticated)
    tutorials = Tutorial.objects.filter(published=True)
    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
