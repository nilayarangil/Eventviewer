from django.db import models

class EventsTb(models.Model):
  EventName = models.CharField(max_length=255)
  EventDesc = models.CharField(max_length=500)
