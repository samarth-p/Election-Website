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

    path('loggedIn_eci/results/const_list/', views.const, name='const'),
    # path('const/<slug:const_id>/', name=)

    path('loggedIn_eci/', views.loggedIn_eci),
    path('loggedIn_eci/results/', views.results),
    path('loggedIn_eci/results/<int:const_id>/result_const/', views.results_const, name='result_const'),
    path('loggedIn_eci/results/result_party/', views.results_party, name='result_party'),
]