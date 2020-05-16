from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import CRUDModel
from .forms import CRUDform

# Create your views here.

def home(request):
    return render(request,'CRUD_app/home.html')

def create(request):
    data={}
    form=CRUDform(request.POST or None)
    if(form.is_valid()):
        form.save()
    data['form']=form
    return render(request,'CRUD_app/index.html',data)    
 
def list(request):
    data={}
    data['context']=CRUDModel.objects.all()
    return render(request,'CRUD_app/list.html',data)

def require(request):
    return render(request,'CRUD_app/search.html')

def req(request):
    return render(request,'CRUD_app/update.html')

def search(request):
    data={}
    try:
        roll2 = request.GET.get('roll')
        data['context']=CRUDModel.objects.filter(roll=roll2)
        return render(request,'CRUD_app/list.html',data)
    except:
        return render(request,'CRUD_app/error.html')
        
        
def update(request):
    data={}
    try:
        roll2=request.GET.get('roll')
        obj=get_object_or_404(CRUDModel,roll=roll2)
        form=CRUDform(request.POST or None,instance=obj)
    
        if(form.is_valid()):
            form.save()
            return redirect('list')
    
        data['form']=form
    except:
        return render(request,'CRUD_app/error.html')
            
    return render(request,'CRUD_app/index.html',data)

def dele(request):
    return render(request,'CRUD_app/delete.html')
        
def delete(request):
    data={}
    try:
        roll2=request.GET.get('roll')
        obj=get_object_or_404(CRUDModel,roll=roll2)
        
        if request.method=="POST":
            obj.delete()
            return redirect('list')
    except:
        return render(request,'CRUD_app/error.html')
        
    return render(request,'CRUD_app/ind.html',data)

 