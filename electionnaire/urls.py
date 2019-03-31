from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('login/confirm/', views.confirm),
    path('loggedIn/', views.loggedIn),
    path('loggedIn/success/', views.success),
    path('loggedIn/<slug:voter_id>/vote/', views.vote, name='vote'),
    path('loggedIn/<slug:voter_id>/process/', views.process_vote, name='process_vote'),
    path("login/eci/", views.eci_login),
    path('loggedIn_eci/', views.loggedIn_eci),
]