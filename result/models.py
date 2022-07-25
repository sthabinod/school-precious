from django.db import models
from account.models import StudentProfile

class Result(models.Model):
    student =  models.ForeignKey(StudentProfile,on_delete=models.DO_NOTHING)
    result = models.FileField()
    year = models.DateField(null=True,blank=True)
    is_pass = models.BooleanField(default=False)