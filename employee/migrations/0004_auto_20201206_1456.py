# Generated by Django 3.1.3 on 2020-12-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_students_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
