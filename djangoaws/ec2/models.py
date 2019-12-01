from typing import List

from django.db import models
from django.contrib.postgres.fields import JSONField


class classproperty:
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)


class InstanceManager(models.Manager):
    def sync(self, instances: List[dict]) -> dict:
        """
        Takes a list of instance data dict's from AWS and saves
        them to the DB
        """
        # purge table
        self.all().delete()

        # bulk create
        self.bulk_create([
            self.model(**{f:data[f] for f in self.model.field_names[1:]})
            for data in instances
        ])

        return {'count': self.count()}


class Instance(models.Model):
    AmiLaunchIndex = models.IntegerField()
    ImageId = models.CharField(max_length=50)
    InstanceId = models.CharField(max_length=50)
    InstanceType = models.CharField(max_length=50)
    KeyName = models.CharField(max_length=50)
    LaunchTime = models.DateTimeField()
    Monitoring = JSONField()

    objects = InstanceManager()

    @classproperty
    def field_names(cls) -> List[str]:
        """Returns the models field names"""
        fields = cls._meta.get_fields()
        return [f.name for f in fields]
