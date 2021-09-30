from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import datetime 
from .models import Subject, Student, Mark


class StudentsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='teststudent',
            email='teststudent@email.com',
            password='test!234'
        )
        self.subject = Subject.objects.create(
            name='Matma'
        )
        self.student = Student.objects.create(
            user= self.user,
            # subjects= [self.subject],
            names="Jan Paweł",
            last_name="Pawlacz",
            father_name="Karol",
            place_of_birth="Wrocław",
            date_of_birth=datetime.datetime(2001,7,13),
            school_class="1C",
            contact_number="999999999"
        )
        # print(self.student.subjects)
        # self.student.subjects.add(self.subject)
        # print(self.student.subjects)
        # s.subjects.set([self.subject])
    
    def test_student_listing(self):
        self.assertEqual(f'{self.student.user}', self.user.username)
        self.assertEqual(f'{self.student.names}','Jan Paweł')
        # self.assertEqual(f'{self.student.subjects}', 'Matma')
        self.assertEqual(f'{self.student.names}','Jan Paweł')
        self.assertEqual(f'{self.student.last_name}',"Pawlacz")
        self.assertEqual(f'{self.student.father_name}',"Karol")
        self.assertEqual(f'{self.student.place_of_birth}',"Wrocław")
        self.assertEqual(f'{self.student.date_of_birth}',
                         f'{datetime.datetime(2001,7,13)}')
        self.assertEqual(f'{self.student.school_class}',"1C")
        self.assertEqual(f'{self.student.contact_number}',"999999999")
    
    def test_student_list_view_for_logged_in_user(self):
        self.client.login(username='teststudent', password='test!234')
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jan Paweł Pawlacz')
        self.assertTemplateNotUsed(response, 'school/school_list.html')