from django.forms import ModelForm, DateInput
from complaintapp.models import Complaint

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        widgets = {'date':DateInput(attrs={'type': 'date', 'id':'date'})}
