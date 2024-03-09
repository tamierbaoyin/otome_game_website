from rest_framework.serializer import ModelsSerializer
from .models import Game, Character

class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'