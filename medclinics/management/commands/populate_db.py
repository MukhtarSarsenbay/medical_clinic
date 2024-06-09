from django.core.management.base import BaseCommand
from medclinics.models import Service, Diagnosis, Appeal
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Services
        services = []
        for _ in range(10):
            service = Service(
                title=fake.word(),
                description=fake.text(),
                price=round(random.uniform(10.0, 1000.0), 2),
                category=fake.word()
            )
            service.save()
            services.append(service)

        # Create Diagnoses
        diagnoses = []
        for _ in range(10):
            diagnosis = Diagnosis(
                title=fake.word(),
                description=fake.text(),
                symptoms=fake.text()
            )
            diagnosis.save()
            diagnoses.append(diagnosis)

        # Create Appeals
        for _ in range(50):
            Appeal.objects.create(
                patient_full_name=fake.name(),
                service=random.choice(services),
                diagnosis=random.choice(diagnoses),
                reason=fake.text(max_nb_chars=100)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
