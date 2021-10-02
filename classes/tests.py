import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Subject, SchoolClass, Mark
from students.models import Student
from teachers.models import Teacher

class TestSchoolClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_student = get_user_model().objects.create_user(
            username='teststudent',
            email='teststudent@email.com',
            password='test!234')
        
        cls.user_teacher = get_user_model().objects.create_user(
            username='testteacher',
            email='testteacher@email.com',
            password='test!234')
        
        cls.student = Student.objects.create(
            user = cls.user_student,
            first_name = 'Tester',
            last_name = 'Studenta',
            sex = 'M')
        
        cls.teacher = Teacher.objects.create(
            user = cls.user_teacher,
            first_name = 'Tester',
            last_name = 'Nauczyciel',
            sex = 'M')
        
        cls.school_class = SchoolClass.objects.create(
            supervising_teacher = cls.teacher,
            first_year = datetime.datetime(2020,9,1),
            name = 'A')
        
        cls.school_class.students.add(cls.student)
        cls.subject = Subject.objects.create(
            name = 'Matematyka')
        cls.mark = Mark.objects.create(
            student = cls.student,
            teacher = cls.teacher,
            subject = cls.subject,
            value = 5,
            weight = 1,
            note = "Notatka testowa")


    def test_subject_listing(self):
        self.assertEqual(self.subject.name, 'Matematyka')


    def test_school_class_listing(self):
        self.assertEqual(f'{self.school_class.students.get(first_name="Tester")}',
                         'Tester Studenta')
        self.assertEqual(f'{self.school_class.supervising_teacher}',
                         'Tester Nauczyciel')
        self.assertEqual(f'{self.school_class.first_year}', 
                         f'{datetime.datetime(2020,9,1)}')
        self.assertEqual(f'{self.school_class.name}', 'A')


    def test_mark_listing(self):
        self.assertEqual(f'{self.mark.student}', 'Tester Studenta')
        self.assertEqual(f'{self.mark.teacher}', 'Tester Nauczyciel')
        self.assertEqual(f'{self.mark.subject}', 'Matematyka')
        self.assertEqual(self.mark.value, 5)
        self.assertEqual(self.mark.weight, 1)
        self.assertEqual(f'{self.mark.note}', "Notatka testowa")
        


