from django.urls import path, include

from claim import views

urlpatterns = [
    path('claim/', views.create_claim, name='create_claim'),
    path('viewClaims/', views.view_claims, name='view_claims'),

]
