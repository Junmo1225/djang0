from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('notes/', views.note_list, name='note_list'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('create_note/', views.create_note, name='create_note'),
    path('', views.note_list, name='list'),
    path('about/', views.about, name='about'),
    # path('search_note/', views.search_note, name='search_note'),
    # path('login/', views.login, name='login'),
]