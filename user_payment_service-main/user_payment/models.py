from django.db import models

# Create your models here.


class AppointmentPayment(models.Model):
    card_number = models.CharField(max_length=16)
    
    #expiry_month = models.IntegerField()
   # expiry_year = models.IntegerField()
   # cvc = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    patient_id = models.IntegerField()
    appointment_id = models.IntegerField(unique=True)
    status = models.CharField(max_length=30)
    
    

    def __str__(self):
        return f"Payment: {self.amount} {self.currency}"
