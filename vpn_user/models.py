from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    active = models.BooleanField()
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=75)
    note = models.TextField()
    quota_cycle = models.PositiveSmallIntegerField(default=120) # Unit: hour.
    quota_bytes = models.PositiveIntegerField(default=1)
    enabled = models.BooleanField()

class Log(models.Model):
    username = models.CharField(max_length=32)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    trusted_ip = models.CharField(max_length=64)
    trusted_port = models.PositiveSmallIntegerField()
    protocol = models.CharField(max_length=10)
    remote_ip = models.CharField(max_length=64)
    remote_netmask = models.CharField(max_length=64)
    bytes_received = models.PositiveIntegerField()
    bytes_sent = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField()
