from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Project, Skill, ContactMessage
from .serializers import (
    ProjectSerializer,
    SkillSerializer,
    ContactMessageSerializer,
)

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]


class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]