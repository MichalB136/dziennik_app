import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        get_user_model(), 
        on_delete=models.CASCADE,)
    names = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    school_class = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=12)
    profile_pic = models.ImageField(default='profile_pic/def_profile_pic.jpg', 
                                    upload_to='profile_pic/')

    def __str__(self):
        return self.names + ' ' + self.last_name

    def display_contact_number(self):
        return self.contact_number[0:3] + '-' \
            + self.contact_number[3:6] + '-' \
            + self.contact_number[6:9]