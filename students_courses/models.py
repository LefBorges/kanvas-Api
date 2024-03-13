from django.db import models
from uuid import uuid4


class StudantStutusCourse(models.TextChoices):
    PEDDING = 'pending'
    ACCEPTED = 'accepted'


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(choices=StudantStutusCourse.choices, max_length=11, default=StudantStutusCourse.PEDDING)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='students_courses')
    student = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='students_courses')
