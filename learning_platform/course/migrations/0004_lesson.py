# Generated by Django 3.2.5 on 2022-12-04 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('short_description', models.TextField(blank=True, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=20)),
                ('lesson_type', models.CharField(choices=[('article', 'Article'), ('quiz', 'quiz'), ('exam_prep', 'exam_prep')], default='article', max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course.course')),
            ],
        ),
    ]
