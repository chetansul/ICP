
# Create your models here.
from dateutil.relativedelta import relativedelta
from django.db import models
import uuid
#from user.models import profile
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.
class drugs(models.Model):
    #user = models.ForeignKey(profile, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField("Mobile", max_length=15, validators=[MinLengthValidator(10), MaxLengthValidator(13)], default='')
    Productname = models.CharField(max_length=158)
    batch=models.CharField(max_length=200)
    mfg=models.DateField("Manufacture Date",null=True)
    expirydate=models.DateField("Expiry Date",null=True)
    packmaterial=models.CharField("Package Material" ,max_length=158)

    def __str__(self):
        return self.Productname

class stability(models.Model):
    stability_id = models.AutoField(primary_key=True)
    stab_name = models.CharField(max_length=158)


    def __str__(self):
        return self.stab_name

    
class zone(models.Model):
    zone_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=158,null=True,)

    def __str__(self):
        return self.name



class result(models.Model):

    id=models.AutoField(primary_key=True)
    drug=models.OneToOneField(drugs,on_delete=models.CASCADE)
    zone=models.ForeignKey(zone,on_delete=models.CASCADE)
    stabilities = models.ManyToManyField(stability)
    alert_date=models.DateField("Alert Date", null=True)
    temp = models.CharField(max_length=150,default='0')
    humidity = models.CharField(max_length=158, default='0')


    def save(self, *args, **kwargs):
        self.temp += str("°C ± 2°C")
        self.humidity += str("% RH ± 5% RH")

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.drug)


'''

        if self.stability.stab_name == 'long_term':
            self.alert_date += relativedelta(months=12) # for days we can use (days=365)
        elif self.stability.stab_name == 'accelerated':
            self.alert_date += relativedelta(months=6)# for days we can use (days=)
        elif self.stability.stab_name == 'intermediate':
            self.alert_date += relativedelta(months=6)# for days we can use (days=180)

'''