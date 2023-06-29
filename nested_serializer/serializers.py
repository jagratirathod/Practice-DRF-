from rest_framework import serializers
from .models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True, read_only=True)
    # sungby = serializers.StringRelatedField(many=True)
    # sungby = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # sungby = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='sungby-detail')   //not working
    # sungby = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')

    class Meta:
        model = Singer
        fields = ['name', 'gender', 'sungby']

    def create(self, validated_data):
        sungby_data = validated_data.pop('sungby')
        singer = Singer.objects.create(**validated_data)
        for song_data in sungby_data:
            Song.objects.create(singer=singer, **song_data)
        return singer

    
  