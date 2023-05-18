from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="login"),
    path("verify/", views.UserVerify.as_view(), name="verify"),
    path("authorization/", views.HomeView.as_view(), name="authorization"),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("create/", views.PostCreate.as_view()),
    path("read/<int:pk>/", views.PostRead.as_view()),
    path("update/<int:pk>/", views.PostUpdate.as_view()),
    path("delete/<int:pk>/", views.PostDel.as_view()),
]
