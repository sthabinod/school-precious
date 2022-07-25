from statistics import mode
from django.db import models






class AboutSchool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("Website Description")
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural="Basic Information"



