from django.urls import path
from . import views

urlpatterns = [
    path('', views.Employees.index, name='index'),
    # path('loginCheck', views.HomePage.checkLogin, name='checkLogin'),
    # path('employee_create', views.HomePage.Singhup, name='singhupEmployee'),
    # path('save_emplyee', views.HomePage.Store, name='save_emplyee'),
]
