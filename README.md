# Readme

Python3 project that sync's AWS data to a Django Postgres DB

# Project Setup

Install project

```
git clone https://github.com/aaronlelevier/djangoaws.git`
cd djangoaws
python3 -m venv venv
pip install -r requirements.txt
```

Then, create Postgres database

```
$ psql
CREATE DATABASE djangoaws
\q
```

Next, migrate initial Django schema

```
./manage.py makemigrations
./manage.py
```

# Usage

Here is some example usage

```python
import boto3
import os

from ec2.models import Instance

client = boto3.client('ec2',
    aws_access_key_id=os.environ['aws_access_key_id'],
    aws_secret_access_key=os.environ['aws_secret_access_key'],
    region_name='us-east-2')

resp = client.describe_instances()

instances = [x for inst in resp['Reservations'] for x in inst['Instances']]

Instance.objects.sync(instances)
```

# Testing

```
# from where manage.py lives
cd ../djangoaws/djangoaws
py.test
```

# License

MIT