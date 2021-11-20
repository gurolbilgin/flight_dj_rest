from django.urls import path
from django.urls.conf import include

from .views import RegisterApi

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("register/", RegisterApi.as_view()),
]
