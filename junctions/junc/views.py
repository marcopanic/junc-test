from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models 

# Create your views here.

class JuncList(ListView):
    model = models.Junction
    select_related = ('corr', 'mark')