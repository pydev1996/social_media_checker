from django.db import models

import datetime
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
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
    status_date = models.CharField(max_length=50,default=d1,null=True)
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
    PRIORITY_CATEGORIES = [
        ("Fake Facebook Accounts in the name of the Bangladesh Army", "Fake Facebook Accounts in the name of the Bangladesh Army"),
        ("Fake Facebook Accounts in the name of the Bangladesh Navy", "Fake Facebook Accounts in the name of the Bangladesh Navy"),
        ("Fake Facebook Accounts in the name of Rapid Action Battalion", "Fake Facebook Accounts in the name of Rapid Action Battalion"),
        ("Fake Facebook Accounts in the name of the Bangladesh AirForce", "Fake Facebook Accounts in the name of the Bangladesh AirForce"),
        ("Anti-State Facebook Accounts related to Chittagong Hill Tracks", "Anti-State Facebook Accounts related to Chittagong Hill Tracks"),
        ("Anti-State Facebook Accounts of Terrorism/Harassment/Religious incitement and others", "Anti-State Facebook Accounts of Terrorism/Harassment/Religious incitement and others"),
    ]

    priority_category = models.CharField(max_length=100, choices=PRIORITY_CATEGORIES)
    SUBCATEGORIES = [
        ('ID', 'ID'),
        ('Page', 'Page'),
        ('Group', 'Group'),
        ('Links', 'Links'),
    ]

    subcategory = models.CharField(max_length=50, default='', null=True, choices=SUBCATEGORIES)
    status_date = models.CharField(max_length=50,default=d1,null=True)
    status = models.CharField(max_length=50,default='',null=True)
    def __str__(self):
        return self.url
