from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomePage.index, name='index'),
    path('loginCheck', views.HomePage.checkLogin, name='checkLogin'),
    path('employee_create', views.HomePage.Singhup, name='singhupEmployee'),
    path('employee_store', views.HomePage.Store, name='EmployeeStore'),
]
