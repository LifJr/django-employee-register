from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_employee, name='employee_insert'),
    path('delete/<int:id>/', views.delete_employee, name='employee_delete'),
    path('<int:id>/', views.form_employee, name='employee_update'),
    path('list/', views.list_employee, name='employee_list'),
    
]
