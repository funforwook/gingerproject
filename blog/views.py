from django.shortcuts import render
from .models import Favorite, Save

# Create your views here.
def index(request):
    context=dict()
    return render(request,'index.html',context)

def create(rqeuqest):
    context=dict()
    return redner(request, 'index.html',context)