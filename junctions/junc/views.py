from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, Count
from . import models
from junc.models import Junction


# Create your views here.

class JuncList(ListView):
    model = models.Junction
    select_related = ('corr', 'mark')

    
    
    count_pr = Junction.objects.aggregate(pk = Count('status', filter=Q(status=Junction.PUN_REZIM)))
    count_pt = Junction.objects.aggregate(pt = Count('pk', filter=Q(status=Junction.PART_TIME)))
    count_ns = Junction.objects.aggregate(ns = Count('pk', filter=Q(status=Junction.NEMA_STRUJE)))
    count_isk = Junction.objects.aggregate(isk = Count('pk', filter=Q(status=Junction.UGASENA)))
    extra_context = {'pr':count_pr,
               'pt':count_pt,
               'ns':count_ns,
               'isk':count_isk,
               'ime':'djuuura',
        }
        
    #return render(request, 'junc/junction_list.html', {'pr':count_pr})
    
class JuncDetail(DetailView):
    model = models.Junction
    select_related = ('corr', 'mark')



class JuncAlldet(ListView):
    model = models.Junction
    select_related = ('corr', 'mark')
    template_name = 'junc/junction_all_detail.html'


class JuncCreate(CreateView):
    model = models.Junction
    fields = ('corr', 'mark','status','needs','civil_works_need','cables_cut','add_info')
    success_url = reverse_lazy('junc:all')


class JuncUpdate(UpdateView):
    template_name = 'junc/junction_update.html'
    model = models.Junction
    fields = ('corr', 'mark','status','needs','civil_works_need','cables_cut','add_info')
    #fields = {'corr':'koridor', 'mark':'oznaka','status':'stanje','needs':'potreba','civil_works_need':'gradj. radovi','cables_cut':'iseceni kablovi','add_info':'dodatni info'}
    
    success_url = reverse_lazy('junc:all')

    # class Meta:
        
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.fields['add_info'].label = 'Dodatne'
            

class JuncDelete(DeleteView):
    model = models.Junction
    success_url = reverse_lazy('junc:all')
    