from __future__ import unicode_literals

from django.db import models

class Film(models.Model):
    pid = models.IntegerField(unique=True)
    picurl = models.CharField(db_column='picUrl', max_length=100)  # Field name made lowercase.
    url = models.CharField(max_length=100)
    realurl = models.CharField(db_column='realUrl', max_length=1000)  # Field name made lowercase.
    videobackimg = models.CharField(db_column='videoBackImg', max_length=100)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    actorname = models.CharField(db_column='actorName', max_length=100)  # Field name made lowercase.
    actorimg = models.CharField(db_column='actorImg', max_length=100)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'film'

class Tags(models.Model):
    pid = models.IntegerField()
    tag = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'tags'


