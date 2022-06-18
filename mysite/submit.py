from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
#from . import simpleform
#from .forms import NameForm


class SimpleForm (forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
def get (request):
   
    return render (request, 'process.html', {'form': form})
    
def post (request):
#class process_form (forms.form):
        #request.submit = submit
 
#TO DO: https://www.tutorialspoint.com/django/django_form_processing.htm
    if request.method == 'GET':
        form=SimpleForm() 
        text= 'enter' 
        return render (request, 'process.html', {'form': form, 'text': text})  
    
    elif request.method == 'POST':
        form=SimpleForm (request.POST)
        
        #subject = forms.cleaned_data['username'] 
        
        if form.is_valid():
            name= form.cleaned_data['username']
            pass1= form.cleaned_data['password']
            
            return render (request, 'process.html', {'form': form, 'text': name, 'word': pass1})
            #return HttpResponseRedirect('/thanks/')
    else:
        form = ""   
        
    #return render (request, 'process.html', {'form': form, 'text': text})
#console log in Python