from django.urls import path, include

from organization import views

urlpatterns = [
    path('organization/', views.create_organization, name='create_organization'),
    path('viewOrganizations/', views.view_organizations, name='view_organizations'),
    path('updateOrganization/<int:organization_id>',
         views.update_organization, name='update_organization'),
    path('getOrganizationInsurances/<int:organization_id>', views.get_organization_insurances,
         name='get_organization_insurances'),

]
