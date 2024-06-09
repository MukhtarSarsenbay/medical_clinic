from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Service, Diagnosis, Appeal

class ModelTests(TestCase):
    def setUp(self):
        self.service = Service.objects.create(title="Test Service", description="Description", price=100, category="Test")
        self.diagnosis = Diagnosis.objects.create(title="Test Diagnosis", description="Description", symptoms="Symptoms")
        self.appeal = Appeal.objects.create(patient_full_name="John Doe", service=self.service, diagnosis=self.diagnosis, reason="Test Reason")

    def test_service_creation(self):
        self.assertEqual(self.service.title, "Test Service")

    def test_diagnosis_creation(self):
        self.assertEqual(self.diagnosis.title, "Test Diagnosis")

    def test_appeal_creation(self):
        self.assertEqual(self.appeal.patient_full_name, "John Doe")

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.service = Service.objects.create(title="Test Service", description="Description", price=100, category="Test")
        self.diagnosis = Diagnosis.objects.create(title="Test Diagnosis", description="Description", symptoms="Symptoms")
        self.appeal = Appeal.objects.create(patient_full_name="John Doe", service=self.service, diagnosis=self.diagnosis, reason="Test Reason")

    def test_get_services(self):
        response = self.client.get(reverse('service-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_diagnoses(self):
        response = self.client.get(reverse('diagnosis-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_appeals(self):
        response = self.client.get(reverse('appeal-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
