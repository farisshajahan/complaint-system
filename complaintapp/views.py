from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from complaintapp.models import Complaint
from complaintapp.forms import ComplaintForm
from notifyapp.main import Email, SMS


class ComplaintView(CreateView):
    model = Complaint
    form_class = ComplaintForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        Email(**form.cleaned_data)
        SMS()
        return super(ComplaintView, self).form_valid(form)
