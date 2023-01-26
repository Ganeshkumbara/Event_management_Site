from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns =[
    path('', RedirectView.as_view(url='home')), 
    path('home', views.home, name='Home' ),
    path('email', views.email, name = 'email'),
    # path('filteredTheme', views.Theme_details.as_view()),
    path('home/<slug>', views.theme_deatils, name ='theme_detail'),
    path('filteredTheme', views.filteredTHeme, name = 'filteredTheme'),
    

]

