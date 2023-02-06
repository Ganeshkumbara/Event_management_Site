from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns =[
    path('', RedirectView.as_view(url='home')), 
    path('home', views.home, name='Home' ),
    path('email', views.email, name = 'email'),
    path('Femail', views.femail, name = 'femail'),
    path('home/<slug>/<category>/<region>', views.theme_deatils, name ='theme_detail'),
    path('filtered', views.filtered , name='Home' ),
    path('contactUs', views.contactUs , name='ContactUs' ),

    # path('filteredTheme', views.Theme_details.as_view()),
    # path('filteredTheme', views.filteredTHeme, name = 'filteredTheme'),
    # path('regionalwiseThemes', views.regionalTheme, name = 'regionalwiseThemes'),
]

