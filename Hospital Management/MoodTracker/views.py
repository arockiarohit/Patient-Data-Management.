from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect



def homepage(request):
    return render(request,"home.html")


@login_required(login_url="/")
def displaypage(request):
    
    context={
        "alldetails1" : information_db.objects.all()
    }
    return render(request, "display.html", context)


@login_required(login_url="/")
def add_data(request):


    context={
        "addproduct1" : DataForm()
    }
    if request.method == "POST":

        product_value = DataForm(request.POST)

        if product_value.is_valid():

            product_value.save()
            return redirect("display")
    
    return render(request, "addproduct.html",context)



@login_required(login_url="/")
def Update_information(request,id):
    selected_row=information_db.objects.get(id = id)

    context={
        "addproduct1":DataForm(instance=selected_row)
    }
    
    if request.method == "POST":
        product_value=DataForm(request.POST,instance=selected_row)

        if product_value.is_valid():
            product_value.save()

        return redirect("add_data1")    
    return render(request,"addproduct.html",context)


@login_required(login_url="/")
def Delete_information(request, id):
    selected_row = get_object_or_404(information_db, id=id)
    selected_row.delete()
    return redirect("display")

###################################################################################################

@login_required(login_url="/")
def hospital_info(request):
    return render(request, "entry.html")



@login_required(login_url="/")
def patient_data(request):


    context={
        "addproduct2" : DataForm1()
    }
    if request.method == "POST":

        product_value = DataForm1(request.POST)

        if product_value.is_valid():

            product_value.save()
            return redirect("patient_display_physical")
           
    
    return render(request, "patient.html",context)


@login_required(login_url="/")
def display_patient(request):

    context={
    "all_details" : Patient_db.objects.all()
    }
    
   

    return render (request,"patient_display.html",context)


@login_required(login_url="/")
def Update_patient(request,id):
    selected_row=Patient_db.objects.get(id = id)

    context={
        "addproduct1":DataForm1(instance=selected_row)
    }
    
    if request.method == "POST":
        product_value=DataForm1(request.POST,instance=selected_row)

        if product_value.is_valid():
            product_value.save()

        return redirect("patient_display_physical")    
    return render(request,"patient.html",context)




@login_required(login_url="/")
def Delete_patient(request, id):
    patient = get_object_or_404(Patient_db, id=id)
    patient.delete()
    return redirect("patient_display_physical")