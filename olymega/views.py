from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
#
# class IndexView(generic.ListView):
#     template_name = 'olymega/index.html',

def index(request):
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    # return render(request, 'olymega/index.html', {'posts': posts})
    return render(request, 'olymega/index.html')



def news(request):
    return render(request, 'olymega/news.html')

def events(request):
    return render(request, 'olymega/events.html')

def join(request):
    return render(request, 'olymega/join.html')

def contact(request):
    return render(request, 'olymega/contact.html')

def bylaws(request):
    return render(request, 'olymega/bylaws.html')

def donate(request):
    return render(request, 'olymega/donate.html')

def forum(request):
    return render(request, 'olymega/forum.html')

def projects(request):
    return render(request, 'olymega/projects.html')
