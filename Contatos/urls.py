from django.urls import path
from Contatos import views

app_name='contatos'

urlpatterns = [
    path('listas/',views.PsicologoListView.as_view(), name='lista-psicologos'),
    path('',views.PsicologoListView.as_view(),name="home-psicologos"),
    path('cria/', views.PsicologoCreateView.as_view(),name="cadastro"),
    path('atualiza/<int:pk>/', views.PsicologoUpdateView.as_view(),name="atualiza"),
    path('apaga/<int:pk>/', views.PsicologoDeleteView.as_view(),name="apaga"),

]
