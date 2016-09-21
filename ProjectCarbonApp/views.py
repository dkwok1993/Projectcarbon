from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ProjectCarbonApp.models import *
from ProjectCarbonApp.forms import *
from django.http import HttpResponseRedirect

import csv
from collections import defaultdict


def index(request):
    context = {}
    context['test_msg'] = 'hi'
    return render(request, 'index.html', context)

def report_one_view(request):
    context = {}
    context['test_msg'] = 'hi this is report 1'
    return render(request, 'report_one.html', context)

def add_report_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file']
            reader = csv.DictReader(request.FILES['file'])
            for row in reader:
                item_id=row['Item']
                name=row['Name']
                purchase_unit=row['Purchase Unit']
                unit = row['Unit']
                item = Item(item_id=item_id, name=name,purchase_unit=purchase_unit, units=unit)
                item.save()
            form = UploadFileForm()
            success_msg = 'success file uploaded'
            return render(request, 'add_report.html', {'form': form, 'success_msg': success_msg})
            
            
    else:
        form = UploadFileForm()
    return render(request, 'add_report.html', {'form': form})


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
            
        return render(request, 'weights.html', context)

def supplier_specific_view(request):
        context = {}
        context['test_msg'] = 'hi this is supplier specific'
        
        supplier_specific = Supplier_specific.objects.all()
        context['supplier_specific'] = supplier_specific
        
        if request.method == 'POST':
            form = supplierspecificForm(request.POST)
            context['form'] = form
            if form.is_valid():
                Supplier_specific.objects.create(name=request.POST['name'],supplier_emission_factor=request.POST['supplier_emission_factor'])
                return render(request, 'supplier_specific.html', context)
        else:
            form = supplierspecificForm()
            context['form'] = form
        return render(request, 'supplier_specific.html', context)

def travelingmethods_view(request):
        context = {}
        context['test_msg'] = 'hi this is traveling methods'    

        travelingmethods = Vehicles.objects.all()
        context['travelingmethods'] = travelingmethods


        if request.method == 'POST':
            form = VehicleForm(request.POST)
            context['form'] = form
            if form.is_valid():
                Vehicles.objects.create(name=request.POST['vehicle_name'],carbon_emission_factor=request.POST['carbon_emission_factor'])
                return render(request, 'travelingmethods.html', context)
        else:
            form = VehicleForm()
            context['form'] = form
            
        return render(request, 'travelingmethods.html', context)
     
    

def editdata_view(request):
    context = {}
    context['test_msg'] = 'hi this is editdata'
    return render(request, 'editdata.html', context)

def dataabc_view(request):
    context = {}
    context['test_msg'] = 'hi this is dataabc'
    return render(request, 'dataabc.html', context)

