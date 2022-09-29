from django.urls import path

from . import views

app_name = 'blogmanagement'
urlpatterns = [
    path('', views.index, name='index'),
    # path('questions/<int:question_id>/', views.detail, name='questionsdetail'),
    # path('questions/<int:question_id>/results/', views.results, name='results'),
    # path('questions/<int:question_id>/vote/', views.vote, name='vote'),
]