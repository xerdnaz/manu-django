from django.shortcuts import render
from django.http import JsonResponse
from .forms import ClientForm, InsurancePlanForm
from .models import Client, InsurancePlan

from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def clients(request):
    insurance_plans = InsurancePlan.objects.all().order_by('client__last_name')

    context = {
        'clients': insurance_plans
    }
    return render(request, 'clients.html', context)

def addclient(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        insurance_plan_form = InsurancePlanForm(request.POST)

        if client_form.is_valid() and insurance_plan_form.is_valid():
            client = client_form.save()
            insurance_plan = insurance_plan_form.save(client=client, commit=False)
            insurance_plan.save()
            messages.success(request, "Client added successfully")
        else:
            messages.error(request, "There was an error saving the client.")
            print("Client form errors:", client_form.errors)
            print("Insurance plan form errors:", insurance_plan_form.errors)
    else:
        client_form = ClientForm()
        insurance_plan_form = InsurancePlanForm()

    return render(request, 'addclient.html', {'client_form': client_form, 'insurance_plan_form': insurance_plan_form})




    
