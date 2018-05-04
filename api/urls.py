from django.urls import path

from api import views

urlpatterns = [
    path('devices/', views.DeviceListView.as_view()),
    path('employees/', views.EmployeeListView.as_view())    
]
