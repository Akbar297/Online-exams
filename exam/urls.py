from django.urls import path
from .views import ExamViewSet, QuestionViewSet, SubjectViewSet, AnswerViewSet

urlpatterns = [
    path('create/exam/', ExamViewSet.as_view({'post': 'create'})),

    path('create/question/', QuestionViewSet.as_view({'post': 'create'})),

    path('create/subject/', SubjectViewSet.as_view({'post': 'create'})),
    path('subjects/', SubjectViewSet.as_view({'get': 'list'})),

    path('create/answer/', AnswerViewSet.as_view({'post': 'create'})),
    path('answers/', AnswerViewSet.as_view({'get': 'list'})),
]
