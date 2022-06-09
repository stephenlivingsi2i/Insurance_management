from django.urls import path

from property import views

urlpatterns = [
    path('property/<int:employee_id>/', views.create_property, name='create_property'),
    path('viewPropertyById/<int:employee_id>/', views.view_property_by_id, name='view_property_by_id'),

]