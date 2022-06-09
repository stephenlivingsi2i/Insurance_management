from django.urls import path

from family import views

urlpatterns = [
    path('family/', views.add_relation, name='add_relation'),
    path('viewFamily/<int:employee_id>/', views.view_family, name='view_family'),
    path('updateRelation/<int:family_id>/', views.update_relation, name='update_relation'),

]