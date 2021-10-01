from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Teacher
class TeacherTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='teststudent',
            email='teststudent@email.com',
            password='test!234'
        )
        self.teacher = Teacher.objects.create(
            user = self.user,
            first_name = 'Tester',
            last_name = 'Testowy',
            sex = 'M'
        )

    def test_teacher_listing(self):
        self.assertEqual(f'{self.teacher.user.username}', self.user.username)
        self.assertEqual(f'{self.teacher.first_name}', 'Tester')
        self.assertEqual(f'{self.teacher.last_name}', 'Testowy')
        self.assertEqual(f'{self.teacher.sex}', 'M')
        
