from django.db import models
from authentication.models import User


class Exam(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Subject(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


QUESTION_TYPE_CHOICES = (
    (1, 'open'),
    (2, 'multiple_choice')
)


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.PositiveIntegerField(choices=QUESTION_TYPE_CHOICES, default=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Answer by {self.student.username} for question {self.question.id}"


class StudentAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)
    choices = models.ForeignKey(Choice, blank=True, null=True, on_delete=models.SET_NULL)
    open_answers = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.user
