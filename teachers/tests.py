from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Teacher


class TeacherTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='teachertest',
            email='teachertest@email.com',
            password='test!234'
        )
        self.teacher = Teacher.objects.create(
            user = self.user,
            first_name = 'Tester',
            last_name = 'Testowy',
            sex = 'M'
        )

    def test_teacher_listing(self):
        self.assertEqual(f'{self.teacher.user.username}', 'teachertest')
        self.assertEqual(f'{self.teacher.first_name}', 'Tester')
        self.assertEqual(f'{self.teacher.last_name}', 'Testowy')
        self.assertEqual(f'{self.teacher.sex}', 'M')
        
    

    def test_student_info_page_for_logged_in_user(self):
        self.client.login(username='teachertest',
                          password='test!234')
        response = self.client.get(reverse('teacher_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dane nauczyciela:')
        self.assertTemplateUsed(response, 'teacher_home.html')

    def test_student_info_page_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('teacher_home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/teacherinfo/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/teacherinfo/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')
