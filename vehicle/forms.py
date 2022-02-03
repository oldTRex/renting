from django import forms
from .models import Rental, Vehicle

class RentalForm(forms.ModelForm):

    # vehicles = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=  Vehicle.objects.all() ,
    # )

    # vehicle = forms.ModelChoiceField(queryset = Vehicle.objects.all() )

    class Meta:
        model = Rental
        fields = ["date" ,"city" , "vehicle"  ]