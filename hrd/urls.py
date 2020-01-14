from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.Employees.index, name='hrdEmployee'),
    path('employees_create', views.Employees.EmployeeCreate, name='EmployeeCreate'),
    # path('loginCheck', views.HomePage.checkLogin, name='checkLogin'),
    # path('employee_create', views.HomePage.Singhup, name='singhupEmployee'),
    # path('save_emplyee', views.HomePage.Store, name='save_emplyee'),
]
