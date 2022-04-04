from django.urls import path
from .views import SignupView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]