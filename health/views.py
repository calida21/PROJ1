from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import render
from health.models import patient
from health.models import doctor

from django.contrib import messages
def Indexpage(request):
    return render(request,'Index.html')

def Userreg_patient(request):
    if request.method=='POST':
        name=request.POST['name']
        surname=request.POST['surname']
        address=request.POST['address']
        number=request.POST['number']
        emergency_number=request.POST['emergency_number']
        age=request.POST['age']
        health_condition=request.POST['health_condition']
        gender=request.POST['gender']
        email=request.POST['email']
        alternate_email=request.POST['alternate_email']
        username=request.POST['username']
        psw=request.POST['psw']
        patient(name=name,surname=surname,address=address,number=number,emergency_number=emergency_number,age=age,health_condition=health_condition,gender=gender,email=email,alternate_email=alternate_email,username=username,psw=psw).save()
        messages.success(request,'added succesfully')
        # note
        return render(request,'Registration_patient.html')
    else:
        return render(request,'Registration_patient.html')

def loginpage_patient(request):
    if request.method=="POST":
        try:
            Userdetails_patient=patient.objects.get(email=request.POST['email'],psw=request.POST['psw'])
            print("Username: ",Userdetails_patient)
            request.session['email']=Userdetails_patient.email
            return render(request,'Index.html')
        except patient.DoesNotExist as e:
            messages.success(request,'invalid')
    return render(request,'Login_patient.html')

   
# doctor
def Userreg_doctor(request):
        if request.method=="POST":
            full_name=request.POST['full_name']
            hospital_name=request.POST['hospital_name']
            number_doc=request.POST['number_doc']
            email_doc=request.POST['email_doc']
            username_doc=request.POST['username_doc']
            psw_doc=request.POST['psw_doc']
        
            doctor(full_name=full_name,hospital_name=hospital_name,number_doc=number_doc,email_doc=email_doc,username_doc=username_doc,psw_doc=psw_doc).save()
            messages.success(request,'added succesfully')
            # note
            return render(request,'Registration_doctor.html')
        else:
            return render(request,'Registration_doctor.html')

def loginpage_doctor(request):
    

    if request.method=="POST":
        try:
            Userdetails_doctor=doctor.objects.get(email_doc=request.POST['email_doc'],psw_doc=request.POST['psw_doc'])
            print("Username: ",Userdetails_doctor)
            request.session['email_doc']=Userdetails_doctor.email_doc
            return render(request,'doc_mainpage.html')
        except doctor.DoesNotExist as e:
            messages.success(request,'invalid')
            return render(request,'Login_doctor.html')
    else:
        return render(request,'doc_mainpage.html')


# doctor's main page
def doctor_main(request):
    if request.doctor.is_authenticated:
        return render(request,'doc_mainpage.html')
    else:
        return render(request,'Login_doctor.html')

# doctor logout page
def doc_logout_page(request):
    logout(request)
    return render(request,'Login_doctor.html')
