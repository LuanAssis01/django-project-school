from rest_framework import generics
from cursos.models import Avaliacao, Curso
from cursos.serializers import AvaliacaoSerializer, CursoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from cursos.permissions import SuperUSer

# ====================== API V1 ======================

#End points de coleção 
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#Endpoints de individuos
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


#End points de coleção 
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #Listagem de OBJETOS
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.filter()

#Endpoints de individuos
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id = self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


# ====================== API V2 ======================

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    #Permissões
    #permission_classes = (permissions.DjangoModelPermissions,)
    permission_classes = (SuperUSer, permissions.DjangoModelPermissions)

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)

        # Paginação correta
        page = self.paginate_queryset(avaliacoes)
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # Se não houver paginação, retorna todas as avaliações
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


''' VIEWSET PADRÃO:
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''

#VIEWSET CUSTOMIZADO:
class AvaliacaoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
