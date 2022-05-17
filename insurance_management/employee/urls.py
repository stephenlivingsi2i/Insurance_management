from django.urls import path, include

from employee import views

urlpatterns = [
    path('employee/', views.create_employee, name='create_employee'),
    path('viewemployees/', views.view_employees, name='view_employees'),
    path('update/<int:user_id>', views.update_employee, name='update_employee'),
    path('delete/<int:user_id>', views.delete_employee, name='delete_employee'),

]
