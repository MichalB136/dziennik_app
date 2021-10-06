import datetime
from django.db import models
from students.models import Student
from teachers.models import Teacher



class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SchoolClass(models.Model):
    students = models.ManyToManyField(Student)
    supervising_teacher = models.ForeignKey(Teacher, 
                                    on_delete=models.CASCADE, 
                                    default=1, 
                                    related_name='supervising_teacher')
    teachers = models.ManyToManyField(Teacher, related_name='teachers')
    first_year = models.DateField()
    name = models.CharField(max_length=1)

    def __str__(self):
        calc_year = datetime.date.today().year - self.first_year.year
        if calc_year < 3 and calc_year >= 1:
            return f'{calc_year}{self.name}'
        elif calc_year < 1:
            return f'1{self.name}'
        else:
            return 'Graduate'


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()
    weight = models.FloatField()
    note = models.TextField()

    def __str__(self):
        return f'{self.value} from {self.subject}'

