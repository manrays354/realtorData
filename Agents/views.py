from django.shortcuts import render

from rest_framework import viewsets
from .models import Agent, Region
from .serializers import AgentSerializer, RegionSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


