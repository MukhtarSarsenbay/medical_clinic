from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Diagnosis(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    symptoms = models.TextField()

    def __str__(self):
        return self.title

class Appeal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient_full_name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.patient_full_name
