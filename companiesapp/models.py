from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    voen = models.IntegerField(verbose_name = 'Vöen',unique = True)
    name = models.CharField(max_length = 255,verbose_name = "Şirkətin adi")
    ceo_first_name = models.CharField(max_length = 50,verbose_name = "Shirketin Rehberinin adi")
    ceo_last_name = models.CharField(max_length = 50,verbose_name = "Shirketin Rehberinin soyadi")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class AsanImza(models.Model):
    company = models.ForeignKey(Company,on_delete = models.CASCADE)
    asan_imza = models.IntegerField("Asan Imza",unique = True)
    asan_nomre = models.CharField("Asan Nomre",unique = True,max_length = 20)

class CompanyContacts(models.Model):
    __choice = ((1,"Telefon"),
    (2,"Email"),
    (3,"Address"))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    contact_type = models.IntegerField(choices=__choice)
    contact = models.CharField(max_length = 255,verbose_name = "Elaqe")
    
    
