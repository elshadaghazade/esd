from django.contrib.auth.forms import UserCreationForm
from companiesapp.models import Company
from django.forms import ModelForm

class RegisterCompany(UserCreationForm):

    fields = ['username','email']

class CompanyCreate(ModelForm):
    class Meta:
        model = Company
        fields = ['voen','name','ceo_first_name','ceo_last_name']
