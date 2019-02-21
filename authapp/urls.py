from django.urls import path
from .views import *

urlpatterns = [
    path("register/",CompanyRegister.as_view(),name = "company_register")
]