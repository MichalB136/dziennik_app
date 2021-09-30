import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        get_user_model(), 
        on_delete=models.CASCADE,)
    subjects = models.ManyToManyField(Subject)
    names = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    school_class = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=9)
    profile_pic = models.ImageField(default='profile_pic/def_profile_pic.jpeg', 
                                    upload_to='profile_pic/')

    def __str__(self):
        return self.names + ' ' + self.last_name

    def display_contact_number(self):
        return '+48' + ' ' + self.contact_number[0:3] + '-' \
            + self.contact_number[3:6] + '-' \
            + self.contact_number[6:9]
    
    def get_absolute_url(self):
        return reverse('student_detail', kwargs= {'pk': str(self.id)})



class Mark(models.Model):
    subject = models.ForeignKey(Subject, on_delete=CASCADE,)
    student = models.ForeignKey(Student, on_delete=CASCADE,)
    value = models.IntegerField()
    weight = models.FloatField(max_length=3)
    note = models.TextField()

    def __str__(self):
        return f'{self.value} from {self.subject}'
