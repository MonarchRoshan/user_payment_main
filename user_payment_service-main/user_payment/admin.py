from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AppointmentPayment  # Import your model

# Register the Payment model with the admin site
admin.site.register(AppointmentPayment)