# Generated by Django 3.2.5 on 2022-12-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
