from .models import Answer
from django.utils import timezone


# def check_time(func):
#     if func:




# def perform_create(self, serializer):
#     student = self.request.user
#     question = serializer.validated_data['question']
#     if Answer.objects.filter(student=student, question=question).exists():
#         raise serializer.ValidationError("You have already answered this question.")
#     serializer.save(student=student)
