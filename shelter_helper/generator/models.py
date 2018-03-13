# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from docxtpl import DocxTemplate, RichText
class Passport(models.Model):
    #field of passport
    passport_no = models.CharField(max_length=30)
    passport_nation = models.CharField(max_length=100)
    passport_first_name = models.CharField(max_length=100)
    passport_middle_name = models.CharField(max_length=100)
    passport_last_name = models.CharField(max_length=100)
    passport_issue_date = models.CharField(max_length=100)
    passport_expire_date = models.CharField(max_length=100)
    passport_birth = models.CharField(max_length=100)
    passport_sex = models.CharField(max_length=10)

    def add_passport(self):
        self.save()
class ARC(models.Model): 
    #field of the arc
    arc_type_of_job = models.CharField(max_length=200)
    arc_passport_info = models.ForeignKey(Passport, on_delete=models.CASCADE)
    arc_name = models.CharField(max_length=200) #in some condition it maybe different with passport name
    arc_union_no = models.CharField(max_length=200)
    arc_authority = models.CharField(max_length=200)
    arc_data_of_issue = models.CharField(max_length=200)
    arc_purpose_of_residence = models.CharField(max_length=200)
    arc_residence_address = models.CharField(max_length=200)
    
    def add_ARC(self):
        self.save()


