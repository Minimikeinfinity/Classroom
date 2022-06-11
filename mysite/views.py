from django.shortcuts import render
from django.http import HttpResponse
#from . import submit 

def index(request):
    title = "***welcome User***"
    pagecontent = """Information is very important as naviagte throughout our lives.
    <br>
    The next line of information.
    <br>
    Last line.
    """
    
    sidebar = "Sidebar information goes here"
    additional_notes = "Notes"
    
    return render(request, 'base.html', {'title': title, 'pagecontent': pagecontent, 'sidebar': sidebar, 'additional_notes': additional_notes})
#Pass back as a value
    #return render(request, 'submit.html' )
#request.username = variable
#django process form submission request. 


    




