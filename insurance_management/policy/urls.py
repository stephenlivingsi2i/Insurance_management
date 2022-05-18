from django.urls import path

from policy import views

urlpatterns = [
    path('policy/', views.create_policy, name='create_policy'),
    path('viewPolicies/', views.view_policies, name='view_policies'),
    path('updatePolicy/<int:policy_id>', views.update_policy,
         name='update_policy'),

]