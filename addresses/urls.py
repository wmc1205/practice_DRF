from django.urls import path

from addresses import views

urlpatterns=[
    path('addresses/',views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('addresses/login/', views.login),
]