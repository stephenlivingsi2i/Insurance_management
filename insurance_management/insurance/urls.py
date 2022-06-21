from django.urls import path, include

from insurance import views

urlpatterns = [
    path('selfInsurance/', views.self_insurance, name='self_insurance'),
    path('termInsurance/', views.term_insurance, name='term_insurance'),
    path('familyIndividualInsurance/', views.family_individual_insurance,
         name='family_individual_insurance'),
    # path('viewInsurances/', views.view_insurances, name='view_insurances'),
    # path('updateInsurance/<int:insurance_id>',
    #      views.update_insurance, name='update_insurance'),

]
