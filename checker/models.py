from django.db import models

import datetime

class SocialMediaURL(models.Model):
    whoposturl = models.URLField(default='')
    whoscreenshotimage = models.ImageField(upload_to='screenshots/', default='')
    hisposturl = models.URLField(null=True)
    hisscreenshotimage = models.ImageField(upload_to='screenshots/', null=True)
    reasonforreporting = models.TextField(null=True)
    specificcause = models.TextField(null=True)
    violated_law = models.TextField(null=True)
    proposed_action = models.TextField(null=True)
    date = models.DateField(default=datetime.date.today)
    status_date = models.CharField(max_length=50,default='',null=True)
    status=models.CharField(max_length=255, default='',null=True)


    def __str__(self):
        return self.hisposturl


class facebookURL(models.Model):
    date = models.DateField(default=datetime.date.today)
    url = models.URLField()
    screenshot_image = models.ImageField(upload_to='screenshots/')
    reason_of_reporting = models.TextField()
    specific_cause = models.TextField()
    digital_act = models.TextField()
    imp_person_category = models.CharField(max_length=100)
    priority_category = models.CharField(max_length=100)
    subcategory=models.CharField(max_length=50,default='',null=True)
    status_date = models.CharField(max_length=50,default='',null=True)
    status = models.CharField(max_length=50,default='',null=True)
    def __str__(self):
        return self.url
