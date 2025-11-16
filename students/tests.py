from django.test import TestCase

# Create your tests here.

from .models import Student

class StudentTest(TestCase):

    def test_create_student(self):
        student = Student.objects.create(
            name="Charlie",
            address="Algeria",
            moyenne=15.5
        )
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(student.name, "Charlie")
