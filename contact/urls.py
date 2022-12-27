from django.urls import path
from contact import views


urlpatterns = [
    path('', views.contact, name='contact'),
    path('inquiry', views.inquiry, name='inquiry')
]