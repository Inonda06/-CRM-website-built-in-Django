
from contextvars import Context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Lead,Agent
from .forms import LeadForm, LeadModelForm

def Landingpage(request):
    return render(request,"Landing.html")

def Lead_List(request):
    lead= Lead.objects.all()
    context= {"lead": lead }
    return render(request, "leeds/Lead_List.html", context)

def Lead_details(request, pk):
    details= Lead.objects.get(id=pk)
    context={"details": details}
    return render(request,'leeds/Lead_details.html', context) 

def Lead_Create(request):
    form=LeadModelForm()
    if request.method =="POST":
        form= LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context= {"form": LeadModelForm()}   

    return render(request, "leeds/Lead_Create.html", context)


#def Lead_Create(request):
    form=LeadModelForm()
    if request.method =="POST":
        form= LeadModelForm(request.POST)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            Last_name= form.cleaned_data['Last_name']
            age=form.cleaned_data['age']
            agent=form.cleaned_data['agent']
            Lead.objects.create(
                first_name=first_name,
                Last_name= Last_name,
                age=age,
                agent=agent
            )
            return redirect('homepage')

    context= {"form": LeadModelForm()}   

    return render(request, "leeds/Lead_Create.html", context)

def Lead_update(request,pk):
    Leads= Lead.objects.get(id=pk)
    form=LeadModelForm(instance=Leads)
    if request.method=="POST":
        form= LeadModelForm(request.POST, instance=Leads)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    context={
        "form":form,
        "Leads": Leads, 
        }
    return render(request,'leeds/Lead_update.html', context) 

def Lead_delete(request,pk):
    Leads= Lead.objects.get(id=pk)
    Leads.delete()
    return redirect("homepage")

