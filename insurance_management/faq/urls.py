from django.urls import path

from faq import views

urlpatterns = [
    path('faq/', views.create_faq, name='create_faq'),
    path('viewAnswers/<int:company_id>/', views.view_answers, name='view_answers'),
    path('updateAnswer/<int:faq_id>/', views.update_answer, name='update_answer'),

]