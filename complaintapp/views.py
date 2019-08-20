from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Complaint

class MainView(CreateView):
    model = Complaint
    fields = ['title', 'location', 'description', 'date']
    template_name = 'complaintapp/form.html'
    success_url = '/'
