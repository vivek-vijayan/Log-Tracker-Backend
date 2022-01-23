from pyexpat import features, model
from statistics import mode
from django.db import models
from datetime import datetime, timedelta
import random
import string
import time

# Create your models here.

class LXL_License(models.Model):
    # License Generator
    def License_Key_Generator(length:int) -> str:
        licensekey = str(hash(str(datetime.date.today()) + str(time.ctime())))
        licensekey += ''.join((random.choice(string.ascii_uppercase) for x in range(length)))
        return str(licensekey)

    license_id = models.AutoField()
    license_key = models.CharField(max_length=2000, default=License_Key_Generator(1000))
    from_date = models.DateTimeField(auto_now=True)
    till_date = models.DateTimeField(default=datetime.now()+timedelta(days=100))
    status = models.CharField(max_length=5, default = 'active')
    









