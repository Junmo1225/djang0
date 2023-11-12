from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.note_list, name='note_list'),
    # path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    # path('create_note/', views.create_note, name='create_note'),
    # path('search_note/', views.search_note, name='search_note')
]