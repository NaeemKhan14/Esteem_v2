from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class room(models.Model):
    room_no = models.AutoField(primary_key=True)
    room_name = models.TextField(max_length = 40)


class plugs(models.Model):
    plug_no = models.AutoField(primary_key=True)
    plug_name = models.TextField(max_length = 40)
    plug_model_name = models.TextField(max_length = 40)
    room_no = models.ForeignKey(room, default=1, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    ip_address = models.TextField(max_length = 40,default="0.0.0.0")


class plug_electricity_consumption(models.Model):
    plug_no = models.ForeignKey(plugs, default=1,on_delete=models.CASCADE)
    Watt = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


# Second part
class energy_generation(models.Model):
    e_id = models.AutoField(primary_key=True)
    name = models.TextField()


class energy_mode(models.Model):
    mode_id = models.TextField(max_length = 4)


class battery(models.Model):
    e_id = models.ForeignKey(energy_generation, default=1,on_delete=models.CASCADE)
    capacity = models.DecimalField(max_digits=20, decimal_places=2)
    current_charge = models.DecimalField(max_digits=3, decimal_places=2)
    current_capacity = models.DecimalField(max_digits=20, decimal_places=2)
    maximum_capacity = models.DecimalField(max_digits=20, decimal_places=2)


class power_transaction(models.Model):
    e_id = models.ForeignKey(energy_generation, default=1,on_delete=models.CASCADE)
    transfer = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


class power_generation(models.Model):
    e_id = models.ForeignKey(energy_generation, default=1, on_delete=models.CASCADE)
    current_power = models.DecimalField(max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

#Storing leaderborad for user
class leaderboard(models.Model):
    entry_no = models.AutoField(primary_key=True)
    plug_no = models.ForeignKey(plugs, default=1,on_delete=models.CASCADE)
    start_time_stamp = models.DateTimeField(auto_now_add=True)
    end_time_stamp = models.DateTimeField(null=True, default=None)
    user_id = models.ForeignKey(User, default=1,on_delete=models.CASCADE)

class user_ranking(models.Model):
    user_id = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    total_KwH = models.DecimalField(max_digits=20, decimal_places=2)
