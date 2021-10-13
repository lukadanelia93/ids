from django.shortcuts import render
from idsapp.models import idcards
# Create your views here.

def index(request):
    siaa = idcards.objects.all()
    context = {
        'siaa': siaa
    }
    return render(request, 'index.html', context)