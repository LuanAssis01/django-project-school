from django.urls import path
from cursos.views import AvaliacaoAPIView, AvaliacoesAPIView, CursoAPIView, CursosAPIView, AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='cursos_avaliacoes'),
    path('cursos/<int:pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes')

]
