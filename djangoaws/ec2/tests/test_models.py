import datetime
from dateutil.tz import tzlocal
import unittest

import pytest

from ec2 import models


# example code of how to use



class InstanceManagerTests(unittest.TestCase):

    @pytest.mark.django_db
    def test_sync(self):
        instances = [{
            'AmiLaunchIndex': 0,
            'ImageId': 'ami-290743',
            'InstanceId': 'i-83535bb',
            'InstanceType': 't2.micro',
            'KeyName': 'my-instance',
            'LaunchTime': datetime.datetime(2019, 11, 30, 17, 13, 27, tzinfo=tzlocal()),
            'Monitoring': {'State': 'disabled'}
        }]

        ret = models.Instance.objects.sync(instances)

        assert ret == {'count': 1}


class InstanceTests(unittest.TestCase):

    def test_field_names(self):
        ret = models.Instance.field_names
        assert ret[1:3] == ['AmiLaunchIndex', 'ImageId'], \
            "smoke test assert part of list is coming back"
