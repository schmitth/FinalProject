from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('images/', views.images_view, name='images'),
    path('sources/', views.read_view, name='read'),
    path('create/', views.create_view, name='create'),
    path('update/', views.update_view, name='update'),
    path('delete/', views.delete_view, name='delete')
]
