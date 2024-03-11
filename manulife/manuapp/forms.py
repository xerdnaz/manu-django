from django import forms
from django.forms import ModelForm
from datetime import datetime

from .models import Client, InsurancePlan, Product, Riders

def calculate_age(birthdate):
    today = datetime.now().date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class ClientForm(ModelForm):
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"})) 
    middle_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Middle Name", "class": "form-control"}), required=False) 
    birthdate = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "placeholder": "Birthdate", "class": "form-control"}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Contact Number", "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Age", "class": "form-control", "readonly": "readonly"}), required=False)
   
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'middle_name', 'birthdate', 'mobile_number', 'email', 'age']

    def clean(self):
        cleaned_data = super().clean()
        birthdate = cleaned_data.get('birthdate')
        if birthdate:
            age = calculate_age(birthdate)
            cleaned_data['age'] = age
        return cleaned_data



class InsurancePlanForm(ModelForm):
  product = forms.ModelChoiceField(widget=forms.Select(attrs={"placeholder": "Policy Plan", "class": "form-control"}), queryset = Product.objects.all(), initial = 0,)
  rider1 = forms.ModelChoiceField(widget=forms.Select(attrs={"placeholder": "Riders", "class": "form-control"}), queryset = Riders.objects.all(), required=False)
  rider2 = forms.ModelChoiceField(widget=forms.Select(attrs={"placeholder": "Riders", "class": "form-control"}), queryset = Riders.objects.all(), required=False)
  rider3 = forms.ModelChoiceField(widget=forms.Select(attrs={"placeholder": "Riders", "class": "form-control"}), queryset = Riders.objects.all(), required=False)
  rider4 = forms.ModelChoiceField(widget=forms.Select(attrs={"placeholder": "Riders", "class": "form-control"}), queryset = Riders.objects.all(), required=False)
  rider5 = forms.ModelChoiceField(widget=forms.Select(attrs={"placeholder": "Riders", "class": "form-control"}), queryset = Riders.objects.all(), required=False)
  rider1_amount = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder": "Rider Amount", "class": "form-control"}), required=False)
  rider2_amount = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder": "Rider Amount", "class": "form-control"}), required=False)
  rider3_amount = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder": "Rider Amount", "class": "form-control"}), required=False)
  rider4_amount = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder": "Rider Amount", "class": "form-control"}), required=False)
  rider5_amount = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder": "Rider Amount", "class": "form-control"}), required=False)
  face_amount = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder": "Face Amount", "class": "form-control"}))
  policy_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Policy Number", "class": "form-control"}))
#   number_of_years = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Number of Years", "class": "form-control"}))
  status = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Status", "class": "form-control"}))
  
  
  class Meta:
    model = InsurancePlan
    fields = "__all__"

  def save(self, client=None, commit=True):
    # Create an instance of the InsurancePlan without saving it to the database
    insurance_plan = super().save(commit=False)
        
    # Associate the client with the insurance plan
    insurance_plan.client = client
        
    if commit:
        insurance_plan.save()
    return insurance_plan
    

