from django import forms
import datetime
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminTimeWidget,AdminDateWidget
#import html5.forms.widgets as html5_widgets
#from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'dateinput', 'readonly':'true'})
#time_widget = forms.widgets.TimeInput(attrs={'class': 'timepicker', 'readonly':'true'})
#time_widget.format = '%I:%M %p'




class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    #Transaccion = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
