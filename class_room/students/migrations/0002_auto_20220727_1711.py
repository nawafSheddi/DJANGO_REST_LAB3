# Generated by Django 3.2.14 on 2022-07-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='GPA',
            field=models.FloatField(default=5),
        ),
        migrations.AddField(
            model_name='students',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='first_name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='students',
            name='last_name',
            field=models.CharField(default='', max_length=15),
        ),
    ]