from rest_framework import status
from exceptions.error_codes import ErrorCodes
from exceptions.exceptions import CustomApiException
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import User
from drf_yasg import openapi
from .serializer import UserRegisterSerializer, UserLoginSerializer


class UserViewSet(ViewSet):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={201: UserRegisterSerializer(), 400: 'Bad Request'},
        operation_summary="Register a new user",
        operation_description="This register for teachers and students.",
    )
    def register(self, request):
        data = request.data
        user = User.objects.filter(username=data.get('username')).first()
        if user:
            raise CustomApiException(error_code=ErrorCodes.ALREADY_EXISTS)
        serializer = UserRegisterSerializer(data=data)
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        responses={201: UserLoginSerializer(), 400: 'Bad Request'},
        operation_summary="Login a students and teachers",
        operation_description="This login for students and teachers.",
    )
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message=serializer.errors)

        data = request.data
        user = User.objects.filter(username=data.get("username")).first()
        if not user:
            raise CustomApiException(error_code=ErrorCodes.USER_DOES_NOT_EXIST)
        if data.get('password') != user.password:
            raise CustomApiException(error_code=ErrorCodes.VALIDATION_FAILED, message={'INCORRECT_PASSWORD'})

        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.acces_token)}, status=status.HTTP_200_OK)
