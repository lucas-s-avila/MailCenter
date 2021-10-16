from django.urls import path

from dashboard import views

urlpatterns = [
    path('email/<int:email_id', views.update_status, name='status')
]
