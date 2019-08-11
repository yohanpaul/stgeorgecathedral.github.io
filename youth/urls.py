from django.conf.urls import url
from django.contrib.auth import views as auth_views

from youth.views import *

urlpatterns = [
    url(r'^home/', HomeView.as_view(), name = "home"), 
    url(r'^login', auth_views.LoginView.as_view(template_name='youth/login.html'), name='login'),
    url(r'^survey-form', SurveyFormView.as_view(), name='survey-form'),
]