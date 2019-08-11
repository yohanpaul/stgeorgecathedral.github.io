# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

PROFESSION = (("1","Study"),
            ("2","Job"),
            )

EDUCATION = (("PG","PG"),
            ("DIPLOMA","DIPLOMA"),
            ("UG","UG"),
            )

STAY_STATUS = (("1","KERALA"),
            ("2","Out of kerala"),
            ("3","Out of India"),
            )

HOME_HOSTEL = (("1","Home"),
            ("2","Hostel"),
            )

AVAILABILITY = (("1","once in a year"),
            ("2","Once in a month"),
            ("3","Once in a week"),
            )


class Ward(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class BloodGroup(models.Model):
    blood_group = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.blood_group

class Profession(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class YouthDetails(models.Model):
    name = models.CharField(max_length=100)
    ward = models.ForeignKey(Ward)
    Region = models.ForeignKey(Region)
    age = models.IntegerField()
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.ForeignKey(BloodGroup, null=True, blank=True)
    phone_number = models.CharField(max_length=100)
    married = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    house_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    father_job = models.ManyToManyField(Profession, null=True, blank=True, related_name='father_profession')
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_job = models.ManyToManyField(Profession, null=True, blank=True, related_name='mother_profession')
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50, choices=PROFESSION)
    education = models.CharField(max_length=50, choices=EDUCATION, null=True, blank=True)
    job = models.ManyToManyField(Profession, null=True, blank=True)
    instituition = models.CharField(max_length=100, null=True, blank=True)
    place_of_stay = models.CharField(max_length=50, null=True, blank=True)
    stay_status = models.CharField(max_length=50, choices=STAY_STATUS, null=True, blank=True) 
    home_hostel = models.CharField(max_length=50, choices=HOME_HOSTEL, null=True, blank=True) 
    availability = models.CharField(max_length=50, choices=AVAILABILITY, null=True, blank=True) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0}_{1}".format(self.name, self.ward)






