from django.urls import path, include

from employee import views

urlpatterns = [
    path('employee/', views.create_employee, name='create_employee'),
    path('viewemployees/', views.view_employees, name='view_employees'),
    path('update/<int:user_id>', views.update_employee, name='update_employee'),
    path('delete/<int:user_id>', views.delete_employee, name='delete_employee'),
    path('getEmployeeInsurances/<int:employee_id>', views.get_employee_insurances,
         name='get_employee_insurances'),
    path('claimDetails/<int:employee_id>/', views.get_claim_details,
         name='get_claim_details'),
    path('particularClaimDetails/<int:employee_id>/<int:insurance_id>/',
         views.get_particular_claim_details, name='get_particular_claim_details'),
    path('getParticularEmployeeInsurance/<int:employee_id>/<int:insurance_id>/',
         views.get_particular_employee_insurance,
         name='get_particular_employee_insurance'),

]
