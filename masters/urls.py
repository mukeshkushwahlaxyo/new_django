from django.urls import path
from . import views

urlpatterns = [
    path('', views.Masters.index, name='masters'),  
    path('department', views.Department.index, name='department'),  
    path('department/create', views.Department.create, name='department.create'),  
    path('department/edit/<int:id>', views.Department.edit, name='department.edit'),  
    path('department/delete/<int:id>', views.Department.delete, name='department.delete'),  
    
    path('documenttype/', views.DocumentType.index, name='document'),  
    path('documenttype/create', views.DocumentType.create, name='document.create'),  
    path('documenttype/edit/<int:id>', views.DocumentType.edit, name='document.edit'),  
    path('documenttype/delete/<int:id>', views.DocumentType.delete, name='document.delete'),  
    
    path('emp_designation/', views.Designation.index, name='emp_designation'),
    path('emp_designation/create', views.Designation.create, name='emp_designation.create'),
    path('emp_designation/edit/<int:id>', views.Designation.edit, name='emp_designation.edit'),
    path('emp_designation/delete/<int:id>', views.Designation.delete, name='emp_designation.delete'),

    path('emp_grade/', views.Grade.index, name='emp_grade'),
    path('emp_grade/create', views.Grade.create, name='emp_grade.create'),
    path('emp_grade/edit/<int:id>', views.Grade.edit, name='emp_grade.edit'),
    path('emp_grade/delete/<int:id>', views.Grade.delete, name='emp_grade.delete'),

    path('emp_status/', views.EmpStatus.index, name='emp_status'),
    path('emp_status/create', views.EmpStatus.create, name='emp_status.create'),
    path('emp_status/edit/<int:id>', views.EmpStatus.edit, name='emp_status.edit'),
    path('emp_status/delete/<int:id>', views.EmpStatus.delete, name='emp_status.delete'),

    path('emp_type/', views.EmpType.index, name='emp_type'),
    path('emp_type/create', views.EmpType.create, name='emp_type.create'),
    path('emp_type/edit/<int:id>', views.EmpType.edit, name='emp_type.edit'),
    path('emp_type/delete/<int:id>', views.EmpType.delete, name='emp_type.delete'),
]