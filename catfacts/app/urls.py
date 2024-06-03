from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SingUpView.as_view(), name='signup'),
]