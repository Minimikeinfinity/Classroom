from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

#from .forms import NameForm
def login(request):
    title = "This is the login page"
    return render(request, 'login.html', {'title': title})



def process_form (request):
        #request.submit = submit
    
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        subject = form.cleaned_data['username']
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST) Reuse
        print("Goodbye cruel world!", file=sys.stderr)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = ""   
        
    return render (request, 'submit.html')