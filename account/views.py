import datetime
from django.contrib import auth
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from account.models import Bus, Chat, EntranceRegister, ParentProfile, ScholarshipRegister, TeacherLeave
from django.conf import settings
import random
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from decorators import allowed_users
def register_entrance(request):
    try:    
        if request.method == "POST":
            full_name = request.POST.get("full_name") 
            image = request.POST.get('image')
            gender = request.POST.get("gender")
            father_name = request.POST.get("father_name") 
            mother_name = request.POST.get("mother_name") 
            guardian_contact = request.POST.get("guardian_contact") 
            phone_number = request.POST.get("phone_number") 
            date_of_birth= request.POST.get("date_of_birth") 
            school = request.POST.get("school") 
            grade = request.POST.get("grade") 
            faculty = request.POST.get("faculty") 
            entrance = EntranceRegister.objects.create(full_name = full_name,image=image,gender=gender,
            father_name=father_name,mother_name=mother_name,
            guardian_contact=guardian_contact,
            phone_number=phone_number,date_of_birth=date_of_birth,school=school,grade=grade,faculty=faculty)
            entrance.save()
            messages.success(request, 'Application form is registered successfully!')

        else:
            print("Not a post method")
          
        return render(request,"account/entrance_register.html")
    except Exception as error:
        messages.error(request,error)
    return render(request,"account/entrance_register.html")


def scholarship(request):
    try:    
        if request.method == "POST":
            full_name = request.POST.get("full_name") 
            image = request.POST.get('image')
            gender = request.POST.get("gender")
            father_name = request.POST.get("father_name") 
            mother_name = request.POST.get("mother_name") 
            guardian_contact = request.POST.get("guardian_contact") 
            phone_number = request.POST.get("phone_number") 
            date_of_birth= request.POST.get("date_of_birth") 
            school = request.POST.get("school") 
            grade = request.POST.get("grade") 
            faculty = request.POST.get("faculty") 
            entrance = ScholarshipRegister.objects.create(full_name = full_name,image=image,gender=gender,
            father_name=father_name,mother_name=mother_name,
            guardian_contact=guardian_contact,
            phone_number=phone_number,date_of_birth=date_of_birth,school=school,grade=grade,faculty=faculty)
            entrance.save()
            messages.success(request, 'Scholarship form is registered successfully!')

        else:
            print("Not a post method")
          
        return render(request,"account/scholarship_register.html")
    except Exception as error:
        messages.error(request,error)
    return render(request,"account/scholarship_register.html")


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def apply_leave(request):
    try:    
        if request.method == "POST":
            reason_of_leave = request.POST.get("reason") 
            days = request.POST.get('days')
            teacher_user = get_object_or_404(User,pk=request.user.id)
            leave = TeacherLeave.objects.create(reason_of_leave = reason_of_leave,number_of_days=days,teacher_user=teacher_user)

            leave.save()
            messages.success(request, 'Leave applied successfully, wait for approvement.')

        else:
            print("Not a post method")
          
        return render(request,"account/apply_leave.html")
    except Exception as error:
        messages.error(request,error)
    return render(request,"account/apply_leave.html")

def login_user(request):
    if request.method == 'POST':
        # Getting from post request
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # Checking if the user exists in database
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username,password=password)
            # Checking if user is active or not
            if user is None:
                print("Hereeee")

                messages.error(request, "User not found!")
                return redirect('login')
            else:
                # Calling login function and redirect to home page
                login(request,user)
                return redirect('index')
        else:
            messages.error(request, 'Username or password does not matched!')
    else:
        print("This is not POST method")
    return render(request, 'account/login.html')

def activate(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password = request.POST.get("password")
        c_password = request.POST.get("c_password")
        email = request.POST.get('email')
        print(email,password,username)
        if password == c_password:
            if User.objects.filter(username=username,email=email).exists():
                messages.error(request, "User already exists!")
            else:
                print("User is found!")
                user = User.objects.create(username=username,email=email)
                user.set_password(password)
                user.save()             
                messages.success(request, "User id is created, try logging in using:- " + user.username)
                
        else:
            print('Password error')
            messages.error(request, 'Password does not match eachother!')
        
    return render(request, "account/activate.html")

@login_required(login_url='login')
def logout_user(request):
    try:
        logout(request)
        return redirect('index')
    except Exception:
        messages.error("Something went wrong while logging out! Please try again and contact admin.")

@login_required(login_url='login')
def edit(request,id):
    person = Person.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST.get("phone")
        temp_address= request.POST.get("temporary_address")
        permanent_address = request.POST.get("permanent_address")
        birth_place = request.POST.get('birth_place')
        file = request.POST.get('file')
        date_of_birth = request.POST.get('date_of_birth')
        person_obj = Person.objects.filter(id=id).update(date_of_birth=date_of_birth, temporary_address=temp_address,permanent_address=permanent_address,
                    file=file,phone_number=phone,birth_place=birth_place)
        messages.success(request, "Profile edited successfully!")
        return redirect('details',id=id)
    data = {
        'person':person
    }

    return render(request, "account/edit_profile.html",data)


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def my_leave(request):
    leave = None    
    try:
        leave = TeacherLeave.objects.filter(teacher_user=request.user.id)
        messages.success(request, "Your leaves!")
    except Exception as ex:
        messages.error(request,ex)
    print(leave)        
    data = {
        'leaves':leave
    }


    return render(request, "account/my_leave.html",data)



@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def send_mail_bus_user(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message= request.POST.get("message")
        email_list = []
        bus =Bus.objects.all()
        for b in bus:
            email_list.append(b.user.email)
        
        print(email_list)
        send_mail(
                subject,
                message,
                'stha.binod1000@gmail.com',
                email_list,
                fail_silently=False,
            )
        print("* * ** * * * ** * * * * * * *Email Sent * ** * * * ** * * * * * * * * ** * *")
        messages.success(request, "Email Sent!")
        return redirect('home')
    else:
        return redirect('email_form')



    
def email_form(request):

    return render(request, "account/bus_user_notice.html")


    
def unauthorized(request):

    return render(request, "unauthorized.html")

    
def chat(request):
    parent = ParentProfile.objects.all()
    chat = Chat.objects.all()

    data = {
        'parent':parent,
        
    }
    return render(request, "chatting.html",data)

