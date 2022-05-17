from django.urls import path, include

from insurance import views

urlpatterns = [
    path('insurance/', views.create_insurance, name='create_insurance'),
    path('viewInsurances/', views.view_insurances, name='view_insurances'),
    path('updateInsurance/<int:insurance_id>',
         views.update_insurance, name='update_insurance'),

]
