from django.urls import path
from .views import CompanyView

#Se Crean la Rutas necesarias  id para Delete y update 
urlpatterns=[
    path('companies/',CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(), name='companies_process')
]