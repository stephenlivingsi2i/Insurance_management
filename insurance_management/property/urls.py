from django.urls import path

from property import views

urlpatterns = [
    path('property/', views.create_property, name='create_property'),
    path('viewPropertyById/', views.view_property_by_id, name='view_property_by_id'),

]