from django.urls import path

from . import views

app_name = 'blogmanagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blog, name='blogs'),
    path('blog-detail/<str:blog_slug>/', views.blog_detail, name='blog-detail'),
    
    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact'),
    path('our-services/', views.services, name='our-services'),
    path('portfolio/', views.portfolio, name='portfolio'),

    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    
   # path('questions/<int:question_id>/', views.detail, name='questionsdetail'),
    # path('questions/<int:question_id>/results/', views.results, name='results'),
    # path('questions/<int:question_id>/vote/', views.vote, name='vote'),
]