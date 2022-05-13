from django.urls import path, include

from employee import views

urlpatterns = [
    path('user/', views.create_user, name='create_user'),
    path('usersview/', views.view_user, name='view_user'),
    path('update/<int:user_id>', views.update_user, name='update_user'),
    path('delete/<int:user_id>', views.delete_user, name='delete_user'),

]
