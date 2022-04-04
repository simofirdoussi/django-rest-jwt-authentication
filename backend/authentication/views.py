from django.shortcuts import render
from rest_framework.exceptions import APIException

class DuplicateException(APIException):
    status_code = 303
    default_detail = 'There is already a user with that email'
    default_code = 'Useralready exists'


from rest_framework.views import APIView
from rest_framework import permissions
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        email = data['email']
        if not request.user.is_authenticated:
            if User.objects.filter(email=email).exists():
                print('user exists')
                raise DuplicateException

            e=email.split('@')[0] #first we get the email without the right side of if
            username = ''
            for i in e:
                if i.isalnum():#remove every special character
                    username+=i
            username = username
            username = ''.join([i for i in username if not i.isdigit()]) #delete every number
            user = User.objects.create_user(
                username, email, password=data.get('password')
            )
            user.save()
            refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token)}, safe=False)

#creating a restricted view
from rest_framework_simplejwt.authentication import JWTAuthentication
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        user = request.user
        return JsonResponse({
            'username' : user.username,
            'email' : user.email
        })