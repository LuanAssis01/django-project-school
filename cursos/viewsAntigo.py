from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cursos.models import Avaliacao, Curso
from cursos.serializers import AvaliacaoSerializer, CursoSerializer

class CursoAPIView(APIView):

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_CREATED)



class AvaliacaoAPIView(APIView):

    def get(self, request):
        avalliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avalliacoes, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_CREATED)
