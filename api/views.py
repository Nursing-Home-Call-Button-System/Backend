from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, CallRequest
from .serializers import PatientSerializer, CallRequestSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class CallRequestViewSet(viewsets.ModelViewSet):
    queryset = CallRequest.objects.all()
    serializer_class = CallRequestSerializer
