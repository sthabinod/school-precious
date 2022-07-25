from django.db import models
from django.core.exceptions import ValidationError
import datetime 
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime


GENDER_CHOICES =(
    ("male","male"),
    ("female","female"),
    ("others","others")
)


FACULTY_CHOICES =(
    ("Management","Management"),
    ("Humanities","Humanities")
)

def validate_current_century(date_of_birth):
    if date_of_birth > datetime.date.today():
        raise ValidationError(u'%s is not a valid year!' % date_of_birth)
class Class(models.Model):
    title = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.title


class EntranceRegister(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="entrance", null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='male')
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    guardian_contact = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    date_of_birth = models.DateField(validators=[validate_current_century],null=True,blank=True)
    school = models.CharField(max_length=200)
    grade = models.DecimalField(max_digits=3,decimal_places=2)
    faculty = models.CharField(max_length=100,choices=FACULTY_CHOICES)

    
    class MPTTMeta:
        order_insertion_by = ['full_name']

    def __str__(self) -> str:
        return self.full_name




class ScholarshipRegister(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="entrance", null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='male')
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    guardian_contact = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    date_of_birth = models.DateField(validators=[validate_current_century],null=True,blank=True)
    school = models.CharField(max_length=200)
    grade = models.DecimalField(max_digits=3,decimal_places=2)
    faculty = models.CharField(max_length=100,choices=FACULTY_CHOICES)

    
    class MPTTMeta:
        order_insertion_by = ['full_name']

    def __str__(self) -> str:
        return self.full_name


class TeacherLeave(models.Model):
    reason_of_leave = models.TextField(max_length=250)
    number_of_days = models.IntegerField()
    date_applied = models.DateField(default=datetime.datetime.now())
    teacher_user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    message = models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return str(self.teacher_user.username)

    class Meta:
        verbose_name = "Staff Leave"


class BusCategory(models.Model):
    title = models.TextField(max_length=250)
    description = models.IntegerField()

    def __str__(self):
        return str(self.title)


class Bus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bus_category = models.ForeignKey(BusCategory,on_delete=models.CASCADE)
    bus_point = models.CharField(max_length=100)
    class Meta:
         unique_together = ('user', 'bus_category') 



class ParentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="entrance", null=True,blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='male')
    phone_number = models.CharField(max_length=20, null=True,blank=True)

    
    class MPTTMeta:
        order_insertion_by = ['full_name']

    def __str__(self) -> str:
        return self.full_name


class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="entrance", null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='male')
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    date_of_birth = models.DateField(validators=[validate_current_century],null=True,blank=True)
    faculty = models.CharField(max_length=100,choices=FACULTY_CHOICES)
    parent = models.ForeignKey(ParentProfile,on_delete=models.CASCADE)
    classes = models.OneToOneField(Class,on_delete=models.CASCADE)


    
    class MPTTMeta:
        order_insertion_by = ['full_name']

    def __str__(self) -> str:
        return self.full_name

class TeacherProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="entrance", null=True,blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default='male')
    phone_number = models.CharField(max_length=20, null=True,blank=True)

    
    class Meta:
        verbose_name = "Staff Profile"

    def __str__(self) -> str:
        return self.full_name

    
class Chat(models.Model):
    parent = models.ForeignKey(ParentProfile,on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE)
    message = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.message
