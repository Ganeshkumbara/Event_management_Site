from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Homepage

def home(request):

    themes1 = Homepage()
    themes1.name = "Blue_light princess "
    themes1.price =  5500

    themes2 = Homepage()
    themes2.name = "Blue_light princess "
    themes2.price =  5500
    
    lst = [themes1,themes2]
    return render(request, "index.html",{"lst":lst})







def email(request):
    '''custmer info'''
    email = request.POST['email']
    username = request.POST['name']

    if request.method == "POST":
        subject = 'Django test mail'
        message = (f'Hi {username}, thanks showing interset will get back to u shortly..\n stayed tunned ')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

        return redirect('/')
    return redirect('/')
     