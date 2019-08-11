# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from youth.forms import *

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = "youth/home.html"


class SurveyFormView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'youth/survey_form.html'

    login_url = '/login/'
    form_class = SurveyForm
    success_url = reverse_lazy('survey-form')   
    success_message = "Family details created successfully"
