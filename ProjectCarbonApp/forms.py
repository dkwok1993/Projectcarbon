from django import forms


from django.contrib.auth.models import User
from ProjectCarbonApp.models import *
import re

class LifecycleForm(forms.Form):
    Name123 = forms.CharField(max_length=20)
    carbon_emission_factor  = forms.DecimalField(max_digits=6, decimal_places=3)

    def __init__(self, *args, **kwargs):
        super(LifecycleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'lifecycleForm'
    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(LifecycleForm, self).clean()
        
        name = cleaned_data.get('name')
        carbon_emission_factor = str(cleaned_data.get('carbon_emission_factor'))
        if re.match('^[a-zA-Z\s\w]+$', name) is None:
           raise forms.ValidationError("Please enter numericals for carbon emission factor and the correct item name")

        # We must return the cleaned data we got from our parent.
        return cleaned_data

class supplierspecificForm(forms.Form):
    name = forms.CharField(max_length=20)
    supplier_emission_factor  = forms.DecimalField(max_digits=6, decimal_places=3)

    def __init__(self, *args, **kwargs):
        super(supplierspecificForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'supplierspecificForm'
    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(supplierspecificForm, self).clean()
        name = cleaned_data.get('name')
        supplier_emission_factor = str(cleaned_data.get('supplier_emission_factor'))
        
        if re.match('^[a-zA-Z\s\w]+$', name) is None:
           
            raise forms.ValidationError("Please enter numericals for supplier's carbon emission factor and the correct item name")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


class VehicleForm(forms.Form):
    vehicle_name = forms.CharField(max_length=20)
    carbon_emission_factor  = forms.DecimalField(max_digits=6, decimal_places=3)

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'vehicleForm'
    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(VehicleForm, self).clean()

        vehicle_name = cleaned_data.get('vehicle_name')
        carbon_emission_factor = str(cleaned_data.get('carbon_emission_factor'))

        if re.match('^[a-zA-Z\s\w]+$', vehicle_name) is None:
           
            raise forms.ValidationError("Please enter numericals for carbon emission factor and characters for vehicle name")

        # We must return the cleaned data we got from our parent.
        return cleaned_data

class WeightsForm(forms.Form):
    purchase_unit = forms.CharField(max_length=20)
    purchase_unit_conversion_rate  = forms.DecimalField(max_digits=6, decimal_places=3)

    def __init__(self, *args, **kwargs):
        super(WeightsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'WeightsForm'
    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(WeightsForm, self).clean()

        purchase_unit = cleaned_data.get('purchase_unit')
        purchase_unit_conversion_rate = str(cleaned_data.get('purchase_unit_conversion_rate'))

        if re.match('^[a-zA-Z\s\w]+$', purchase_unit) is None:
           
            raise forms.ValidationError("Please enter characters for purchasing unit and decimals for conversion rate.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data
    
MAX_UPLOAD_SIZE = 2500000


class UploadFileForm(forms.Form):
    file = forms.FileField()
    
    def clean_file(self):
        csv_file = self.cleaned_data['file']
        if not csv_file:
            return None
        if not csv_file.content_type or not csv_file.content_type.endswith('csv'):
            raise forms.ValidationError('File type is not csv')
        if csv_file.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError('File too big (max size is {0} bytes)'.format(MAX_UPLOAD_SIZE))
        return csv_file
