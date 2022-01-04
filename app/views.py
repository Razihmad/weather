from django.shortcuts import render,HttpResponse
import requests
from app.models import Details
from django.core.mail import send_mail
import time

def home(request):
    if request.method=='POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        city = request.POST.get('city')
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=531fd30b5908dad912d0c9b28313a7eb").json()
        temp = data['main']['temp']
        temp = temp-273
        temp = int(temp)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)    
        send_mail(subject=f"Hi {name}, interested in our services",message=f"{temp} Degree Celcius",
                  from_email='admin@tutorchamps.com',fail_silently=False,recipient_list=[f"{email}"])    
        Details(email=email,username=name,city=city,time=current_time).save()
    return render(request,'home.html')