import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import  MinLengthValidator

# Create your models here.
def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')


SEX_CHOICES = (
    ("ma", "Male"),
    ("fe", "Female"),

)


class idcards(models.Model):


    poto = models.ImageField(upload_to="static", default="")  
    cardno = models.CharField(max_length=100, default="")
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    cit = models.CharField(max_length=100, default="")
    sex =  models.CharField(max_length=20, choices=SEX_CHOICES)
    personalno = models.CharField(validators=[only_int,MinLengthValidator(11)],max_length=11, default="") 
    dateofbirth = models.DateField(default=datetime.date.today)
    dateofexpiry = models.DateField(default=datetime.date.today)
    signature = models.CharField(max_length=100, default="")
    placeofbirth = models.CharField(max_length=100, default="")
    dateofissue = models.DateField(default=datetime.date.today)
    issuingauthority = models.CharField(max_length=100, default="")

    
    
    class Meta:
        verbose_name_plural = "idcards"