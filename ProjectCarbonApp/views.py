from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ProjectCarbonApp.models import *
from ProjectCarbonApp.forms import *
from django.http import HttpResponseRedirect


def index(request):
    context = {}
    context['test_msg'] = 'hi'
    return render(request, 'index.html', context)

def report_one_view(request):
    context = {}
    context['test_msg'] = 'hi this is report 1'
    return render(request, 'report_one.html', context)

def add_report_view(request):
    context = {}
    context['test_msg'] = 'hi this is add report'
    return render(request, 'add_report.html', context)

def editdatabase_view(request):
    context = {}
    context['test_msg'] = 'hi this is edit database'
    return render(request, 'editdatabase.html', context)

def lifecycle_view(request):
        context = {}
        context['test_msg'] = 'hi this is lifecycle'
        
        life_cycle = Lifecycle.objects.all()
        context['life_cycle'] = life_cycle
    
        if request.method == 'POST':
            form = LifecycleForm(request.POST)
            context['form'] = form
            if form.is_valid():
                Lifecycle.objects.create(name=request.POST['name'],carbon_emission_factor=request.POST['carbon_emission_factor'])
                return render(request, 'lifecycle.html', context)
        else:
            form = LifecycleForm()
            context['form'] = form
            
        return render(request, 'lifecycle.html', context)

def weights_view(request):
        context = {}
        context['test_msg'] = 'hi this is weights'
    
        weights = Weights.objects.all()
        context['weights'] = weights
    
        if request.method == 'POST':
            form = WeightsForm(request.POST)
            context['form'] = form
            if form.is_valid():
                Weights.objects.create(purchase_unit=request.POST['purchase_unit'],purchase_unit_conversion_rate=request.POST['purchase_unit_conversion_rate'])
                return render(request, 'weights.html', context)
    
        else:
            form = WeightsForm()
            context['form'] = form
            
        return render(request, 'weightsx`.html', {'form': context})

def supplier_specific_view(request):
        context = {}
        context['test_msg'] = 'hi this is supplier specific'
        if request.method == 'POST':
            form = supplierspecificForm(request.POST)
            if form.is_valid():
                Supplier_specifc.objects.create(name=request.POST['name'],supplier_emission_factor=request.POST['supplier_emission_factor'])
                return render(request, 'supplier_specific.html', context)
        else:
            form = supplierspecificForm()
        return render(request, 'supplier_specific.html', {'form': form})

def travelingmethods_view(request):
        context = {}
        context['test_msg'] = 'hi this is traveling methods'    
        if request.method == 'POST':
            form = VehicleForm(request.POST)
            if form.is_valid():
                Vehicles.objects.create(name=request.POST['vehicle_name'],carbon_emission_factor=request.POST['carbon_emission_factor'])
                return render(request, 'travelingmethods.html', context)
        else:
            form = VehicleForm()
        return render(request, 'travelingmethods.html', {'form': form})
     
    

def editdata_view(request):
    context = {}
    context['test_msg'] = 'hi this is editdata'
    return render(request, 'editdata.html', context)

def dataabc_view(request):
    context = {}
    context['test_msg'] = 'hi this is dataabc'
    return render(request, 'dataabc.html', context)

