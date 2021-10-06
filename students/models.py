import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models




class Student(models.Model):
    id = models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)  
    M = 'Male'
    F = "Female"
    SEX_CHOICES = [
        (M, 'Male'),
        (F, 'Female')
    ]
    sex = models.CharField(max_length=6, 
                        choices=SEX_CHOICES, 
                        default=None)
    profile_pic = models.ImageField(upload_to='profile_pic/', 
                                    default='profile_pic/def_profile_pic.jpeg')

    class Meta:
        permissions = [
            ('is_student', 'Can view student home page')
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


student_group, created = Group.objects.get_or_create(name='Student') 
