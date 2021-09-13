from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee_create', views.createEmployee,name='employee_create'),
    path('employee_edit/<str:id>', views.editEmployee,name='employee_edit'),
    path('employee_delete/<str:id>', views.deleteEmployee,name='employee_delete')
]