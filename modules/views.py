from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.db import postgres_lib
import json

@api_view(['GET'])
def getAll(request):
  data = postgres_lib.connect('allModules')
  return Response({
    'status': 200,
    'message': 'OK',
    'data': data,
  })

@api_view(['GET'])
def get(request, id):
  data = postgres_lib.connect('module', id=id)
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
def getStudentModules(request, courseId, studentId):
  data = postgres_lib.connect('studentModules', courseId=courseId, studentId=studentId)
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
def getStudentModulesForTeacher(request, courseLogId):
  data = postgres_lib.connect('studentModulesForTeacher', courseLogId=courseLogId)
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
def updateStudentModule(request, score, moduleLogId):
  data = postgres_lib.connect('updateStudentModule', moduleLogId=moduleLogId, score=score)
  if data != 1:
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
