from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=32)
    passwrod = models.CharField(max_length=128)
    active = models.BooleanField()
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    name = models.TextField()
    email = models.EmailField(max_length=75)
    note = models.TextField()
    quota_cycle = models.PositiveSmallIntegerField()
    quota_bytes = models.PositiveIntegerField()
    enabled = models.BooleanField()

class Log(models.Model):
    username = models.CharField(max_length=32)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    trusted_ip = models.CharField(max_length=64)
    trusted_port = models.PositiveSmallIntegerField()
    protocal = models.CharField(max_length=10)
    remote_ip = models.CharField(max_length=64)
    remote_netmask = models.CharField(max_length=64)
    bytes_received = models.PositiveIntegerField()
    bytes_sent = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField()
