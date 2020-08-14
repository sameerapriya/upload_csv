from django.db import models
from django.contrib.postgres.fields import JSONField
import json
import pandas as pd


class CsvData(models.Model):
    """Model for the data obtained from the respective file"""
    file_name = models.CharField(max_length=255, default='test.csv')
    data = JSONField()  # This particular field is very flexible for storing JSON encoded data.

    def getframe(self):
        data = json.loads(self.data)
        return pd.DataFrame.from_dict(data)
