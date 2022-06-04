from django.shortcuts import render
from django.http import HttpResponse
#from . import submit 

def index(request):
    title = "***New test Page***"
    pagecontent = """Information is very important as naviagte throughout our lives."""
    
    sidebar = "Sidebar information goes here"
    additional_notes = "Notes"
    
    return render(request, 'base.html', {'title': title, 'pagecontent': pagecontent, 'sidebar': sidebar, 'additional_notes': additional_notes})
#Pass back as a value
    #return render(request, 'submit.html' )
#request.username = variable
#django process form submission request. 


    




