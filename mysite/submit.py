from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

#from .forms import NameForm

def process_form (request):
#def process_form (forms.form):
        #request.submit = submit
 
#TO DO: https://www.tutorialspoint.com/django/django_form_processing.htm
    
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        subject = forms.cleaned_data['username'] 
        #Pass back as an HTML
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST) Reuse
        print("Goodbye cruel world!", file=sys.stderr)
        # check whether it's valid:
        if forms.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        forms = ""   
        
    return render (request, 'submit.html')
#console log in Python