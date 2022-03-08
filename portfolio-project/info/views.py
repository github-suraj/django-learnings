from django.shortcuts import render
from .models import Info

# Create your views here.
def homepage(request):
    infos = Info.objects.all()
    data_dict = dict(infos=infos)
    return render(request, 'info/home.html', data_dict)
