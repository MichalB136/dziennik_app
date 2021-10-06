from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from students.models import Student



class HomepageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_student = get_user_model().objects.create_user(
            username='studenttest',
            email='studenttest@email.com',
            password='testpass123')
        
        cls.student = Student.objects.create(
            user = cls.user_student,
            first_name = 'Tester',
            last_name = 'Studenta',
            sex = 'M')


    
    def test_listings(self):
        self.assertEqual(f'{self.user_student.username}', 'studenttest')
        self.assertEqual(f'{self.user_student.email}', 'studenttest@email.com')
        self.assertEqual(f'{self.student.user.username}', 'studenttest')
        self.assertEqual(f'{self.student.first_name}', 'Tester')
        self.assertEqual(f'{self.student.last_name}', 'Studenta')
        self.assertEqual(f'{self.student.sex}', 'M')

    def test_homepage_for_logged_in_user(self):
        self.client.login(username='studenttest', 
                                password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Homepage')
        self.assertTemplateUsed(response, 'home.html')
        

    def test_homepage_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

class StudentPageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_student = get_user_model().objects.create_user(
            username='studenttest',
            email='studenttest@email.com',
            password='test!234')
        
        cls.student = Student.objects.create(
            user = cls.user_student,
            first_name = 'Tester',
            last_name = 'Studenta',
            sex = 'M')

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


class TeacherPageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_teacher = get_user_model().objects.create_user(
            username='teachertest',
            email='teachertest@email.com',
            password='test!234')
        
        cls.teacher = Student.objects.create(
            user = cls.user_teacher,
            first_name = 'Tester',
            last_name = 'Nauczyciel',
            sex = 'M')

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