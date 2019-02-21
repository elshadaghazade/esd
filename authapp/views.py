from django.shortcuts import render
from django.views.generic import TemplateView
from .form import *
# Create your views here.

class CompanyRegister(TemplateView):
    template_name = "register.html"
    
    def get_context_data(self):
        context = super().get_context_data()
        context['userform'] = RegisterCompany
        context['companyform'] = CompanyCreate
        return context