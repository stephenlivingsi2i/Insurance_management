from django.urls import path

from insurance_company import views


urlpatterns = [
    path('company/', views.create_company, name='create_company'),
    path('viewCompanies/', views.view_companies, name='view_companies'),
    path('updateCompany/<int:company_id>',
         views.update_company, name='update_company'),
]