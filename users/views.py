from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.db import postgres_lib
import json

@api_view(['GET'])
def signin(request, username, password):
  data = postgres_lib.connect('signin')
  for i in data:
    if i['username'] == username and i['password'] == password:
      return Response({
        'status': 200,
        'message': 'OK',
        'data': i
      })
  return Response({
      'status': 401,
      'message': 'Unauthorized',
      'data': {}
    })

  return Response({
    'status': 401,
    'message': 'Unauthorized',
    'data': {},
  })

@api_view(['GET'])
def getAll(request):
  data = postgres_lib.connect('allUsers')
  return Response({
    'status': 200,
    'message': 'OK',
    'data': data,
  })

@api_view(['GET'])
def get(request, id):
  data = postgres_lib.connect('user', id=id)
  if len(data) == 0:
    return Response({
      'status': 400,
      'message': 'Bad Request',
      'data': data,
    })
  return Response({
    'status': 200,
    'message': 'OK',
    'data': data,
  })

@api_view(['POST'])
def create(request):
  return Response({"message": "Hello, world!"})

