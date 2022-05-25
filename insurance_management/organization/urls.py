from django.urls import path, include

from organization import views

urlpatterns = [
    path('organization/', views.create_organization, name='create_organization'),
    path('viewOrganizations/', views.view_organizations, name='view_organizations'),
    path('updateOrganization/<int:organization_id>',
         views.update_organization, name='update_organization'),
    path('getOrganizationInsurances/<int:organization_id>',
         views.get_organization_insurances, name='get_organization_insurances'),
    path('getInsurancesByPolicy/<int:organization_id>/<int:policy_id>/',
         views.get_insurances_by_policy, name='get_insurances_by_policy'),
    path('getParticularOrganizationInsurances/<int:organization_id>/<int:employee_id>/',
         views.get_particular_organization_insurance,
         name='get_particular_organization_insurance'),

]
