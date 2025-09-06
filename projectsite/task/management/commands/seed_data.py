from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from task.models import Task, SubTask, Note, Priority, Category

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with fake Tasks, SubTasks, and Notes"

    def handle(self, *args, **kwargs):
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        if not priorities or not categories:
            self.stdout.write(self.style.ERROR(
                "⚠️ Please add Priority and Category records first (e.g. High, Medium, Low, Work, School, etc.)"
            ))
            return

        for _ in range(10):  # generate 10 tasks
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),                 # ✅ task title
                description=fake.paragraph(nb_sentences=3),      # ✅ task description
                status=fake.random_element(                      # ✅ task status
                    elements=["Pending", "In Progress", "Completed"]
                ),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(priorities),
                category=random.choice(categories),
            )

            # Generate subtasks (1–3 per task)
            for _ in range(random.randint(1, 3)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(
                        elements=["Pending", "In Progress", "Completed"]
                    ),
                    parent_task=task,
                )

            # Generate notes (1–2 per task)
            for _ in range(random.randint(1, 2)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

        self.stdout.write(self.style.SUCCESS("✅ Fake data created successfully!"))
