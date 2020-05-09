from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultant/', views.liste_consultant, name='liste_consultant'),
    path('consultant/<int:collaborateurs_id>/', views.collaborateur_detail, name='collaborateur_detail'),
    path('consultant/ajout/', views.collaborateursCreateView.as_view(), name='collaborateursCreateView'),
    path('consultant/ajout/succes/', views.reussite_ajout_collaborateurs, name='reussite_ajout_collaborateurs'),
    path('client/', views.liste_client, name='liste_client'),
    path('client/ajout/', views.clientCreateView.as_view(), name='clientCreateView'),
    path('client/ajout/succes/', views.reussite_ajout_client, name='reussite_ajout_client'),
    path('competence/', views.liste_competence, name='liste_competence'),
    path('competence/ajout/', views.competencesCreateView.as_view(), name='competencesCreateView'),
    path('competence/ajout/succes/', views.reussite_ajout_competence, name='reussite_ajout_competence'),
    path('outil/', views.liste_outil, name='liste_outil'),
    path('outil/ajout/', views.outilsCreateView.as_view(), name='outilsCreateView'),
    path('outil/ajout/succes/', views.reussite_ajout_outil, name='reussite_ajout_outil')
]