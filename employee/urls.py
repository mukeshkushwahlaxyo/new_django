from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.HomePage.index, name='index'),
    path('loginCheck', views.HomePage.checkLogin, name='checkLogin'),
    path('employee_create', views.HomePage.Singhup, name='singhupEmployee'),
    path('logout_view', views.HomePage.logout_view, name='logout_view'),
    path('get_data', views.HomePage.getAlldata, name='get_data'),
    path('apply_leave/', views.HomePage.ApplyLeave, name='ApplyLeave'),
    path('edit_apply_leave/<int:id>', views.HomePage.EditApplyLeave, name='EditApplyLeave'),
    path('delete_leave/<int:id>', views.HomePage.DeleteLeave, name='DeleteLeave'),
    path('show_leave', views.HomePage.ShowLeaves, name='ShowLeaves'),
    path('manage_role', views.HomePage.ManageRoles, name='ManageRoles'),
    path('assign', views.HomePage.AssignRole, name='AssignRole'),
    # path('save_emplyee', views.HomePage.Store, name='save_emplyee'),
]
