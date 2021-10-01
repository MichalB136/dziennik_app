from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Student



class StudentTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='teststudent',
            email='teststudent@email.com',
            password='test!234'
        )
        self.student = Student.objects.create(
            user = self.user,
            first_name = 'Tester',
            last_name = 'Testowy',
            sex = 'M'
        )

    def test_student_listing(self):
        self.assertEqual(f'{self.student.user.username}', self.user.username)
        self.assertEqual(f'{self.student.first_name}', 'Tester')
        self.assertEqual(f'{self.student.last_name}', 'Testowy')
        self.assertEqual(f'{self.student.sex}', 'M')
        
