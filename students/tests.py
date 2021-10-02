from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Student



class StudentTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='teststudent',
            email='teststudent@email.com',
            password='test!234'
        )
        cls.student = Student.objects.create(
            user = cls.user,
            first_name = 'Tester',
            last_name = 'Testowy',
            sex = 'M'
        )

    def test_student_listing(self):
        self.assertEqual(f'{self.student.user.username}', self.user.username)
        self.assertEqual(f'{self.student.first_name}', 'Tester')
        self.assertEqual(f'{self.student.last_name}', 'Testowy')
        self.assertEqual(f'{self.student.sex}', 'M')
        
    def test_student_info_page_for_logged_in_user(self):
        self.client.login(email='teststudent@email.com', 
                          password='testpass!234')
        self.client.logout()
        response = self.client.get(reverse('student_home'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'text')
        self.assertTemplateUsed(response, 'student_home.html')
        
