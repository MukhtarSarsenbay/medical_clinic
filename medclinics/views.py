from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appeal, Service, Diagnosis
from .serializers import AppealSerializer, ServiceSerializer, DiagnosisSerializer
from django.shortcuts import render

class AppealViewSet(viewsets.ModelViewSet):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated]


def dash_example(request):
    return render(request, 'medclinics/dash_example.html')

