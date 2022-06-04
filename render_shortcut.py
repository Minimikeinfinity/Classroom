from django.shortcuts import render

from pages import render_shortcut


def index(request):
    latest_question_list = " Testing Text "
    #context = {'latest_question_list': latest_question_list}
    context = {'latest_question_list': latest_question_list}
    return render(request, 'new_page.html', context)

#change index.html match my html file. 
#remap question object
#https://docs.djangoproject.com/en/4.0/intro/tutorial03/