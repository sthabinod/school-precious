from django.shortcuts import get_object_or_404, render

from decorators import allowed_users

from .models import Result
from account.models import ParentProfile, StudentProfile
from django.contrib.auth.decorators import login_required    

@login_required(login_url='login')
@allowed_users(allowed_roles=['parent'])
def result(request):
    current_user = request.user.id
    parent = get_object_or_404(ParentProfile,pk=current_user)
    student = StudentProfile.objects.filter(parent=parent)
    results = []

    for s in student:
        result = Result.objects.filter(student=s)
        results.append(result)

    print(student)
    
    new_list = []
    for r in results:
        for r_obj in r:
            new_list.append(r_obj)

    print(new_list)

    data = {
        'results':new_list
    }
    return render(request, "result/result.html",data)

