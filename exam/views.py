from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Exam, Question, Answer, Subject, StudentAnswer
from .serializer import ExamSerializer, QuestionSerializer, AnswerSerializer, SubjectSerializer, StudentAnswerSerializer
from rest_framework.viewsets import ViewSet
from exceptions.exceptions import CustomApiException
from exceptions.error_codes import ErrorCodes
from rest_framework import status, viewsets
from rest_framework.response import Response


class SubjectViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create Subject',
        request_body=SubjectSerializer(),
        responses={201: SubjectSerializer()},
    )
    def create(self, request):
        serializer = SubjectSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='List Subjects',
        request_body=SubjectSerializer(),
        responses={200: SubjectSerializer()},
    )
    def list(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExamViewSet(ViewSet):
    swagger_auto_schema(
        operation_summary='Create Exam',
        request_body=ExamSerializer(),
        responses={201: ExamSerializer()},

    )
    def create(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = ExamSerializer(data=data)
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def exam_check(self, request, pk):
        questions = Question.objects.filter(id=pk).first()
        if not questions:
            raise CustomApiException(error_code=ErrorCodes.NOT_FOUND)





class QuestionViewSet(ViewSet):
    swagger_auto_schema(
        operation_summary='Create Question',
        request_body=QuestionSerializer(),
        responses={201: QuestionSerializer()},
        operation_description='Create a Question',
    )

    def create(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnswerViewSet(ViewSet):
    @swagger_auto_schema(
        operation_summary='Create Answer',
        request_body=AnswerSerializer(),
        responses={201: AnswerSerializer()},
        operation_description='Create a Answer',
    )
    def create(self, request):
        data = request.data
        serializer = AnswerSerializer(data=data)
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(data={'result': serializer.data, 'ok': True}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='List Answers',
        request_body=AnswerSerializer(),
        responses={200: AnswerSerializer()},
    )
    def list(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


