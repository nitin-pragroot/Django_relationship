from django.shortcuts import redirect, render

from .models import *

def index(request):
    queryset_one = User.objects.all()
    queryset_two = Page.objects.all()
    context = {
    "table1_list": queryset_one, 
    "table2_list": queryset_two
    }
    return render(request, "index.html", context)