from django.urls import path
from . import views

app_name = 'electionnaire'
urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.login,name="login"),
    path('login/confirm/<int:voter_id>', views.confirm,name="confirm"),
    path('verify/<int:voter_id>',views.verify,name="verify"),
    path('loggedIn/<int:voter_id>/', views.loggedIn,name="loggedIn"),
    path('loggedIn/upload/', views.upload,name="upload"),
    path('loggedIn/<slug:voter_id>/vote/', views.vote, name='vote'),
    path('loggedIn/<slug:voter_id>/process/', views.process_vote, name='process_vote'),
    path('loggedIn_eci/results/const_list/', views.const, name='const'),
    path('loggedIn_eci/', views.loggedIn_eci),
    path('loggedIn_eci/results/', views.results,name="results"),
    path('loggedIn_eci/results/<int:const_id>/result_const/', views.results_const, name='result_const'),
    path('loggedIn_eci/results/result_party/', views.results_party, name='result_party'),
    path('loggedIn/success/', views.success),
    path('loggedIn/vote/', views.vote,name="vote"),
    path("login/eci/", views.eci_login,name="eci_login"),
]


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.login),
#     path('login/confirm/', views.confirm),
#     path('loggedIn/', views.loggedIn),
#     path('loggedIn/success/', views.success),
#     path('loggedIn/<slug:voter_id>/vote/', views.vote, name='vote'),
#     path('loggedIn/<slug:voter_id>/process/', views.process_vote, name='process_vote'),
#     path("login/eci/", views.eci_login),
#     path('loggedIn_eci/', views.loggedIn_eci),

#     path('loggedIn_eci/results/const_list/', views.const, name='const'),
#     # path('const/<slug:const_id>/', name=)

#     path('loggedIn_eci/', views.loggedIn_eci),
#     path('loggedIn_eci/results/', views.results),
#     path('loggedIn_eci/results/<int:const_id>/result_const/', views.results_const, name='result_const'),
#     path('loggedIn_eci/results/result_party/', views.results_party, name='result_party'),
# ]