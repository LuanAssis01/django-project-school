from rest_framework import serializers
from cursos.models import Avaliacao, Curso
from django.db.models import Avg

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
    def validate_avaliacao(self, valor):
        if valor in range(1,5):
            return valor
        raise serializers.ValidationError('A nota da avaliação precisa ser entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer):

    # 1. Nested Relatioship (Relacionamentos N para 1):
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2. HyperLinked Related Field:
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3. Primary Key Releated Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao', 
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
            
        if media is None:
            return 0
        return round(media*2)/2