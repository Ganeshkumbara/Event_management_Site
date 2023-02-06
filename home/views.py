from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Homepage_themes, FHHomepage_themes, FBDHomepage_themes, FCDHomepage_themes

# from django.views.generic import ListView
# from django.http import JsonResponse

Themes_category = ['Bday_Party','Bachelorette','Baby_Shower','Corporate_party']
regionWiseModel = {'All':Homepage_themes,'Banglore':FBDHomepage_themes,'Hyderabad':FHHomepage_themes,'chennai':FCDHomepage_themes}
regions = ['All','Banglore','Hyderabad','chennai']


# functionz
def validator(selected, item_lists):
    output = []
    for item in item_lists:
        if item == selected:
            continue
        else:
            output.append(item)
    return output

# clone themes from Homepage_themes(Base Theme)

def clone(modelname):
    basemodel = Homepage_themes.objects.all()
    for fmodel in basemodel:
        if fmodel.Theme_price >= 15000:
            cloning=modelname(Theme_name = fmodel.Theme_name, Theme_price=fmodel.Theme_price, Theme_discount=fmodel.Theme_discount, Theme_offer=fmodel.Theme_offer, Theme_discription=fmodel.Theme_discription, Theme_image=fmodel.Theme_image, Theme_url=fmodel.Theme_url, Theme_category=fmodel.Theme_category)
            cloning.save()

# function to load home page

def home(request):
    themes =Homepage_themes.objects.order_by('Theme_price').reverse()
    return render(request, "index.html",{"themes":themes, 'Allcategory':Themes_category,'regions':regions})

# function to load region and theme filtered themes
 


def filtered(request):
    selectedcategory = request.POST['category']
    Themez_category = validator(selectedcategory, Themes_category) # list without selected category
    region = request.POST['rthemes']
    cleanedRegions = validator(region, regions) # list without selected selected region
    if bool(region)  and bool(selectedcategory): # + + 
        themes = regionWiseModel[region].objects.filter(Theme_category = selectedcategory).order_by("Theme_price").reverse()
        return render(request, 'index.html',{'themes':themes, 'Allcategory':Themez_category,'regions':cleanedRegions,'Stheme':selectedcategory, 'selectedregion':region })
    elif  bool(region) == False  and bool(selectedcategory): # - +
        themes = Homepage_themes.objects.filter(Theme_category = selectedcategory).order_by("Theme_price").reverse()
        return render(request, 'index.html',{'themes':themes, 'Allcategory':Themez_category,'regions':cleanedRegions,'Stheme':selectedcategory, 'selectedregion':region })
    elif bool(region) and bool(selectedcategory) == False:# + - 
        themes = regionWiseModel[region].objects.order_by("Theme_price").reverse()
        return render(request, 'index.html',{'themes':themes, 'Allcategory':Themez_category,'regions':cleanedRegions,'Stheme':selectedcategory, 'selectedregion':region })
    elif bool(region) == False and bool(selectedcategory) == False: # - -
        themes = Homepage_themes.objects.order_by("Theme_price").reverse()
        return render(request, 'index.html', {'themes':themes, 'Allcategory':Themez_category,'regions':cleanedRegions,'Stheme':selectedcategory, 'selectedregion':region })

# function to load contact us html

def contactUs(request):
    return  render(request, "contactus.html")

# function to load image using slug url

def theme_deatils(request, slug, category, region):
    print(category)
    if region == "Home":
        themes = Homepage_themes.objects.filter(Theme_category=category).order_by('?')[:3]
        theme = Homepage_themes.objects.get(Theme_url = slug)
        return render(request,'test.html',{'theme':theme, 'themes':themes})
    elif region == "Hyderabad":
        themes = FHHomepage_themes.objects.filter(Theme_category=category).order_by('?')[:3]
        theme = FHHomepage_themes.objects.get(Theme_url = slug)
        return render(request,'test.html',{'theme':theme, 'themes':themes})
    elif region == "Bangalore":
        themes = FBDHomepage_themes.objects.filter(Theme_category=category).order_by('?')[:3]
        theme = FBDHomepage_themes.objects.get(Theme_url = slug)
        return render(request,'test.html',{'theme':theme, 'themes':themes})
    elif region == 'Chennai':
        themes = FCDHomepage_themes.objects.filter(Theme_category=category).order_by('?')[:3]
        theme = FCDHomepage_themes.objects.get(Theme_url = slug)
        return render(request,'test.html',{'theme':theme, 'themes':themes})

# Mail function
        
def email(request):
    '''custmer info'''
    useremail = request.POST['email']
    username = request.POST['name']
    time =  request.POST['time']
    ph_number = request.POST['phone']
    user_message = request.POST['message']
    user_event_date = request.POST['date'] 
    if request.method == "POST":
        subject = 'Mr.Air🎉 Balloon Event Management'
        message = (f'Hi {username}, thanks showing interset, will get back to u shortly..\n\n\nstayed tunned😊')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [useremail]
        send_mail( subject, message, email_from, recipient_list )
        send_mail(subject,f'''Custmer:{username} \nDate:{user_event_date}\nTime:{time}\nPh_nor:{ph_number}\nmessage:{user_message}''',email_from,['ganesh700511@gmail.com'])
        return redirect('/home')
    return redirect('/home')
    
def femail(request):
    '''franchise custmer info'''
    inquirer_mailId = request.POST['contact-email']
    inquirer_name = request.POST['contact-name']
    inquirer_ph_number = request.POST['contact-phone']
    inquirer_message = request.POST['contact-message']
    inquirer_region = request.POST['Region']
    inquirer_pincode = request.POST['pincode']
    if request.method == "POST":
        subject = 'Mr.Air🎉 Balloon Event Management'
        message = (f'Hi {inquirer_name}, thanks showing interset, will get back to u shortly..\n\n\nstayed tunned😊')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [inquirer_mailId]
        send_mail( subject, message, email_from, recipient_list )
        send_mail(subject,f'''Custmer:{inquirer_name} \nRegion:{inquirer_region} \nPincode:{inquirer_pincode}\nPh_nor:{inquirer_ph_number}\nmessage:{inquirer_message}''',email_from,['ganesh700511@gmail.com'])
        return redirect('/contactUs')
        