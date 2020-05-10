from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.db import postgres_lib
import json

@api_view(['GET'])
def getAll(request):
  data = postgres_lib.connect('allCourses')
  return Response({
    'status': 200,
    'message': 'OK',
    'data': data,
  })

@api_view(['GET'])
def get(request, id):
  data = postgres_lib.connect('course', id=id)
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

@api_view(['GET'])
def getStudentCourses(request, id):
  data = postgres_lib.connect('studentCourses', id=id)
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

@api_view(['GET'])
def getTeacherCourses(request, id):
  data = postgres_lib.connect('teacherCourses', id=id)
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

@api_view(['GET'])
def getInfo(request, id):
  data = postgres_lib.connect('courseInfo', id=id)
  # print('---------------------')
  # print(data)
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
