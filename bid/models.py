from django.db import models

# Create your models here.
class Bid:
    acc_id = models.CharField(max_length=30)
    bid_value = models.IntegerField(default=0)