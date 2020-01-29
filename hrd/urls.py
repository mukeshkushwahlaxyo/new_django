from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.Employees.index, name='hrdEmployee'),
    path('employees_create', views.Employees.EmployeeCreate, name='EmployeeCreate'),
    path('save_employee', views.Employees.saveEmployee, name='save_employee'),
    path('delete_employee/<int:id>', views.Employees.deleteEmployee, name='delete_employee'),
    path('edit_employee/<int:id>', views.Employees.editEmployee, name='edit_employee'),
    path('showTabs/<slug:page>/<int:id>', views.Employees.showTabs, name='showTabs'),    
]
# /<str:form>/<int:id>