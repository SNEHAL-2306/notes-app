from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'is_important', 'created_at']

