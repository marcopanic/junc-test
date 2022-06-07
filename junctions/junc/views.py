from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from . import models 


# Create your views here.

class JuncList(ListView):
    model = models.Junction
    select_related = ('corr', 'mark')

    
    def count_status(request):
        count_pr = Junction.objects.aggregate(pr = Count('pk', filter=Q(status=Junction.PUN_REZIM)))
        count_pt = Junction.objects.aggregate(pr = Count('pk', filter=Q(status=Junction.PART_TIME)))
        count_ns = Junction.objects.aggregate(pr = Count('pk', filter=Q(status=Junction.NEMA_STRUJE)))
        count_isk = Junction.objects.aggregate(pr = Count('pk', filter=Q(status=Junction.UGASENA)))
        context = {'pr':count_pr,
                    'pt':count_pt,
                    'ns':count_ns,
                    'isk':count_isk,
        }
        
        return render(request, 'junc/junction_list.html', context)
    
