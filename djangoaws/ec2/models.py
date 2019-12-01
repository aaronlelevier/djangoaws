from django.db import models
from django.contrib.postgres.fields import JSONField


class Instance(models.Model):
    AmiLaunchIndex = models.IntegerField()
    ImageId = models.CharField(max_length=50)
    InstanceId = models.CharField(max_length=50)
    InstanceType = models.CharField(max_length=50)
    KeyName = models.CharField(max_length=50)
    LaunchTime = models.DateTimeField()
    Monitoring = JSONField()
