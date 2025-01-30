from rest_framework import serializers
from cursos.models import Avaliacao, Curso

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )

class CursoSerializer(serializers.ModelSerializer):

    # 1. Nested Relatioship (Relacionamentos N para 1):
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2. HyperLinked Related Field:
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3. Primary Key Releated Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao', 
            'ativo',
            'avaliacoes'
        )