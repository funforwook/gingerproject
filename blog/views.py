from django.shortcuts import render, redirect
from .models import Add
from .forms import AddForms
from django.utils import timezone

# Create your views here.
def index(request):
    context=dict()
    all_add = Add.objects.all()
    context['all_add'] = all_add
    print(request.GET)
    context["write_form"] = AddForms()

    return render(request,'index.html',context)

def create(request):
    context=dict()
    if request.method == "POST":
        temp_form = AddForms(request.POST)
        if temp_form.is_valid():
            #add_form = temp_form.save(commit=False) #담아만두기
            #add_form.date = timezone.now() #작성시간만들어주기
            temp_form.save()
            return redirect('index')
        else:
            context["write_form"] = temp_form
            return render(request,'add_cont.html',context)         

def detail(request, add_id):
    context= dict()
    context['detail_add'] = Add.objects.get(id = add_id)
    return render(request, 'detail.html', context)

def update(request, add_id):
    context= dict()
    if request.method == "POST":
        temp_form = AddForms(request.POST,instance=Add.objects.get(id = add_id))
        if temp_form.is_valid():
            temp_form.save()
            return redirect('index')
        else:
            context["write_form"] = temp_form
            return render(request,'add_cont.html',context)
    else:
        context["write_form"] = AddForms(instance=Add.objects.get(id = add_id))
        return render(request, 'add_cont.html', context)



def delete(request, add_id):
    delete_form = Add.objects.get(id = add_id) 
    delete_form.delete()
    return redirect('index')
