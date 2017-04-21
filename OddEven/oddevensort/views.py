# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from batcher_oddeven_multiprocessing import batcher_multiprocessed
# Create your views here.


def index(request):

    if request.method == 'POST':
        inputform = forms.NumbersForm(request.POST)

        if inputform.is_valid():
            inputnumbers = inputform.cleaned_data['inputNumbers']
            unsortednumbers =intConversion(inputnumbers)
            sortednumbers = batcher_multiprocessed(list(unsortednumbers))

            context={
                'numbers':sortednumbers,
            }
            return render(request,'results.html',context)

    else:
        inputform=forms.NumbersForm()

        return render(request,'homepage.html',context={'inputform':inputform,})



def intConversion(charnumbers):
    charnumbers=charnumbers.split(' ')
    numbers=[]
    for c in charnumbers:
        numbers.append(int(c))

    return numbers
