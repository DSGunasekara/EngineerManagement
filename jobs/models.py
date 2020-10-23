from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    date = models.DateField('job date')
    time = models.TimeField('job time')
    status = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    SVR_ID = models.CharField(max_length=200)
    LCON_name = models.CharField(max_length=200)
    LCON_contact_no = models.CharField(max_length=200)

    def __str__(self):
        return self.location


class JobManagement(models.Model):
    fe_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    rate = models.CharField(max_length=5)
    date = models.DateField('job date')
    start_time = models.TimeField('start time')
    end_time = models.TimeField('end time')

    def __str__(self):
        return self.fe_id.name
