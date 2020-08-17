import pathlib

from django.contrib.auth.models import User
from django.db import models


def quiz_image_upload_path(quiz, filename):
    suffix = pathlib.Path(filename).suffix
    return f'images/{quiz.slug}/meta{suffix}'


class Quiz(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to=quiz_image_upload_path,
        null=True, blank=True
    )
    image_blurhash = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


def question_description_image_upload_path(question, filename):
    suffix = pathlib.Path(filename).suffix
    return f'images/{question.quiz.slug}/' + \
           f'questions/{question.id}/description{suffix}'


def question_solution_image_upload_path(question, filename):
    suffix = pathlib.Path(filename).suffix
    return f'images/{question.quiz.slug}/' + \
           f'questions/{question.id}/solution{suffix}'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    description = models.TextField(null=True, blank=True)
    description_image = models.ImageField(
        upload_to=question_description_image_upload_path,
        null=True, blank=True
    )
    description_image_blurhash = models.TextField(null=True, blank=True)

    solution = models.TextField(null=True, blank=True)
    solution_image = models.ImageField(
        upload_to=question_solution_image_upload_path,
        null=True, blank=True
    )
    solution_image_blurhash = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)