from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Homepage_themes
from django.views.generic import ListView

def home(request):
    Allcategory = Homepage_themes.objects.all()
    themes =Homepage_themes.objects.order_by('id')
    
    return render(request, "index.html",{"themes":themes, 'Allcategory':Allcategory})


def theme_deatils(request, slug):
    themes = Homepage_themes.objects.order_by('?')[:3]
    theme = Homepage_themes.objects.get(Theme_url = slug)
    return render(request,'test.html',{'theme':theme, 'themes':themes})

# class Theme_details(ListView):
#     model = Homepage_themes

#     template_name = 'test2.html'
#     queryset = Homepage_themes.objects.filter(id= 6)

def filteredTHeme(request):
    selectedTheme = request.POST['category']
    if request.method == 'POST':
        Allcategory = Homepage_themes.objects.all()
        if selectedTheme != 'All':
            themes = Homepage_themes.objects.filter(Theme_category=selectedTheme)
            return render(request, 'index.html',{'themes':themes, 'Allcategory':Allcategory })
        elif selectedTheme == 'All':
            themes = Homepage_themes.objects.all()
            return render(request, 'index.html',{'themes':themes, 'Allcategory':Allcategory })





def email(request):
    '''custmer info'''
    useremail = request.POST['email']
    username = request.POST['name']
    time =  request.POST['time']
    ph_number = request.POST['phone']
    user_message = request.POST['message']
    user_event_date = request.POST['date']
    if request.method == "POST":
        subject = 'Mr.Air Balloon Event Management'
        message = (f'Hi {username}, thanks showing interset, will get back to u shortly..\n\n\nstayed tunned😊')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [useremail]
        send_mail( subject, message, email_from, recipient_list )
        send_mail(subject,f'''Custmer:{username} \nDate:{user_event_date}\nTime:{time}\nPh_nor:{ph_number}\nmessage:{user_message}''',email_from,['ganesh700511@gmail.com'])
        return redirect('/home')
    return redirect('/home')
     