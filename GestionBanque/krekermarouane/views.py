import code
from multiprocessing import context
from multiprocessing.connection import Client
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator


from .models import Compte
from .models import Client
from .models import Operation
from .forms import ClientForm
from .forms import CompteForm
from .forms import OperationForm

# Create your views here.
def compte_list(request):
    comptes = Compte.objects.all()
    paginator = Paginator(comptes, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'comptes.html', {'page_obj': page_obj})

def details(request, code):
    client = Client.objects.get(code = code)
    context = {'client':client}
    return render(request, 'details.html',context)

def client_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        clients = Client.objects.filter(nom__icontains=q)
    else:
        clients = Client.objects.all()
    context= {'clients': clients }  
    return render(request, 'clients.html', context)

def detailop(request, code):
    operation = Operation.objects.get(client = code)
    context = {'operation':operation}
    return render(request, 'detailsop.html',context)

def Clientform(request):
    formc = ClientForm()
    if request.method == 'POST' :
     formc = ClientForm(request.POST) 
     if formc.is_valid():
         formc.save()
    
    fromcom = CompteForm()
    if request.method == 'POST' :
        fromcom = CompteForm(request.POST) 
        if fromcom.is_valid():
         fromcom.save()
         
    formo = OperationForm()
    if request.method == 'POST' :
        formo = OperationForm(request.POST) 
        if formo.is_valid():
         formo.save()
         
    context = {'formc':formc ,'fromcom':fromcom,'formo':formo}
    return render(request, 'forms.html' , context)
      

