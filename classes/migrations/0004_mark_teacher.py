# Generated by Django 3.2.7 on 2021-10-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('classes', '0003_mark_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
    ]