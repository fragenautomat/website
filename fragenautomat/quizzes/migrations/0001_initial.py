# Generated by Django 3.0.8 on 2020-08-17 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import quizzes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=quizzes.models.quiz_image_upload_path)),
                ('image_blurhash', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_image', models.ImageField(blank=True, null=True, upload_to=quizzes.models.question_description_image_upload_path)),
                ('description_image_blurhash', models.TextField(blank=True, null=True)),
                ('solution', models.TextField(blank=True, null=True)),
                ('solution_image', models.ImageField(blank=True, null=True, upload_to=quizzes.models.question_solution_image_upload_path)),
                ('solution_image_blurhash', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Quiz')),
            ],
        ),
    ]