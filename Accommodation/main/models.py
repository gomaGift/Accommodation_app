from django.db import models  
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Room(models.Model):
    room_number = models.IntegerField()
    hostel = models.CharField(max_length=30)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.hostel} room {self.room_number}"



# Create your models here.
class User(AbstractUser):
    
    ROLES = [
        ('stu', 'STUDENT'),
        ('admin', 'ADMIN')
    ]

    PROVINCES =[ 
        ('east', 'Eastern Province'),
        ('west', 'Western Province'),
        ('south', 'Southern Province'),
        ('muchi', 'Muchinga Province'),
        ('cent', 'Central Province'),
        ('copper', 'CopperBelt'),
        ('northwest', 'North Western'),
        ('lus', 'Lusaka'),
        ('luap', 'Luapula'),
        ('north', 'Nothern Provice'),

    ]
    STATUS = [
        ('dis', 'Disabled'),
        ('norm', 'normal')
    ]

    name = models.CharField(max_length=30, blank=True)
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
    id_num = models.CharField(max_length=10, unique=True)
    user_role = models.CharField(max_length=10, choices=ROLES, default='stu')
    province = models.CharField(max_length=20, choices=PROVINCES)
    status = models.CharField(max_length=15, choices=STATUS, default='norm')
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.name 
    
    def save(self, *args, **kwargs) -> None:
        if not self.name:
          self.name = f"{self.first_name} {self.last_name}"
        if not self.username:
         self.username = self.id_num
        return super().save(*args, **kwargs)


class RoomApplication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reviewed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.name