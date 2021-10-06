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
        self.assertEqual(f'{self.student.user.username}', 'teststudent')
        self.assertEqual(f'{self.student.first_name}', 'Tester')
        self.assertEqual(f'{self.student.last_name}', 'Testowy')
        self.assertEqual(f'{self.student.sex}', 'M')


    def test_student_info_page_for_logged_in_user(self):
        self.client.login(username='studenttest',
                          password='test!234')
        response = self.client.get(reverse('student_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dane studenta:')
        self.assertTemplateUsed(response, 'student_home.html')

    def test_student_info_page_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('student_home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/studentinfo/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/studentinfo/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

        
