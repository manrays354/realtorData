from rest_framework import serializers
from .models import Agent, Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), source='region', write_only=True)

    class Meta:
        model = Agent
        fields = ('id', 'name',  'phone', 'agency', 'sales','experience','activity', 'region', 'region_id')
