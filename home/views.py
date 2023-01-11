from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, "index.html")


def email(request):
    '''custmer info'''
    email = request.POST['email']
    username = request.POST['name']

    if request.method == "POST":
        subject = 'welcome to GFG world'
        message = f'Hi {username}, thanks showing interset will get back to u shortly.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/')
    return redirect('/')
     