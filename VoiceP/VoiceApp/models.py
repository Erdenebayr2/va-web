from django.db import models

class Chat(models.Model):
    userchat = models.CharField(max_length=200)
    aichat = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Chat {self}"
    
class Group(models.Model):
    userchat = models.CharField(max_length=200)
    aichat = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Chat {self}"
