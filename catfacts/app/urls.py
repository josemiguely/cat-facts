from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('catfacts/', views.CatFactsView.as_view(), name='catfacts'),
    path('like_cat_fact/', views.LikeCatFactView.as_view(), name='like_cat_fact'),
    path('liked_facts/', views.LikedFactsView.as_view(), name='liked_facts'),
    path('most-liked-facts/', views.MostLikedFactsView.as_view(), name='most_liked_facts'),
]