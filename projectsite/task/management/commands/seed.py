from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random
from task.models import Task, SubTask, Note, Priority, Category

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with fake data"

    def handle(self, *args, **kwargs):
        # Populate Priority
        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        for p in priorities:
            Priority.objects.get_or_create(name=p)

        # Populate Category
        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        for c in categories:
            Category.objects.get_or_create(name=c)

        # Populate Task, SubTask, Notes
        for _ in range(10):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(
                    elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(Priority.objects.all()),
                category=random.choice(Category.objects.all())
            )

            # Subtasks
            for _ in range(3):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=5),
                    status=fake.random_element(
                        elements=["Pending", "In Progress", "Completed"]),
                    parent_task=task
                )

            # Notes
            for _ in range(2):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )
