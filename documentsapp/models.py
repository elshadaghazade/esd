from django.db import models
from companiesapp.models import Company


class Documents(models.Model):
    __choice = ((1,'Yaradildi'),
    (2,"Gonderen imzaladi"),
    (3,"Qebul eden imzaladi"),
    (4,"Qebul eden imtina etdi"),
    (5,"Vaxti bitib"))
    __doc_type_choice = ((1,"Muqavile"),
    (2,"Hesab Faktura"))
    sender = models.ForeignKey(Company,on_delete = models.CASCADE,related_name="sender_doc_set")
    receiver = models.ForeignKey(Company,on_delete= models.CASCADE,related_name="receiver_doc_set")
    notes = models.CharField(max_length = 255,verbose_name = "Qeydler")
    doc_date = models.DateField()
    doc_expr_date = models.DateField()
    status = models.IntegerField(choices=__choice,default=1)
    doc_send_date = models.DateTimeField(auto_now=True)
    doc_file = models.FileField(upload_to="docs")
    doc_type = models.IntegerField(choices=__doc_type_choice)









