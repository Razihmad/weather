from django.shortcuts import redirect, render,HttpResponse
import requests
from django.contrib import messages
from app.models import Details
from django.core.mail import send_mail
import time

def home(request):
    if request.method=='POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        city = request.POST.get('city')
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=531fd30b5908dad912d0c9b28313a7eb").json()
        if data['cod']==200:
            temp = data['main']['temp']
            temp = temp-273
            temp = int(temp)
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)    
            if temp<=10:
                
                send_mail(subject=f"Hi {name}, interested in our services",message=f"{temp}" +'\N{DEGREE SIGN}' + ' '+'\U0001F976',
                    from_email='admin@tutorchamps.com',fail_silently=False,recipient_list=[f"{email}"])  
            elif 10<temp<28:
                send_mail(subject=f"Hi {name}, interested in our services",message=f"{temp}" +'\N{DEGREE SIGN}' + ' '+'\U0001F60C',
                    from_email='admin@tutorchamps.com',fail_silently=False,recipient_list=[f"{email}"])    
            else:
                send_mail(subject=f"Hi {name}, interested in our services",message=f"{temp}" +'\N{DEGREE SIGN}' + ' '+'\U0001F975',
                    from_email='admin@tutorchamps.com',fail_silently=False,recipient_list=[f"{email}"])  
                
            Details(email=email,username=name,city=city,time=current_time).save()
            messages.success(request,"Temprature of your city has been sent to your mail")
            return redirect('home')
        else:
            messages.warning(request,data['message'])
            return redirect('home')
    return render(request,'home.html')