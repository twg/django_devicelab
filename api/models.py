from django.db import models
from django.contrib import admin

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Device(models.Model):
    name = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    metadata = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ledger(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    device = models.ForeignKey('Device', on_delete=models.PROTECT)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

admin.site.register(Employee)
admin.site.register(Device)
