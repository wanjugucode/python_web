# Generated by Django 4.0.5 on 2022-06-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
