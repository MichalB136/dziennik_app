from django.contrib.auth import get_user_model
from django.db import models


class Notifications(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    note = models.TextField()
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
