from django.db import models
from django.contrib.auth.models import Permission, User

class Constants:
	Vehicle_status=(
		('1', '1'),
		('0', '0'),
		('-1', '-1'),
	)

class Driver_detail(models.Model):
    driver_name=models.CharField(max_length=60)
    driver_contact_number=models.BigIntegerField()
    vehilce_number= models.CharField(max_length=60)
    current_vehicle_location=models.CharField(max_length=60,default='Jabalpur')
    last_stoppage=models.CharField(max_length=60,default='delhi')
    vehicle_status=models.CharField(max_length=10,choices=Constants.Vehicle_status,default='-1')
    distance_covered=models.IntegerField(default=0)
    last_update=models.IntegerField(default=40)

    def __str__(self):
        return self.driver_name     
