from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/<int:id>/', views.detail, name='detail'),
    path('contacts/add/', views.add, name='add'),
    path('contacts/delete/<int:id>/', views.delete, name='delete'),
    path('contacts/edit/<int:id>', views.edit, name='edit'),
    path('about/', views.about, name='about'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_account, name='login'),
    path('accounts/logout/', views.logout_account, name='logout'),
]