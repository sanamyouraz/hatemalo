from django.shortcuts import render,HttpResponse
from .models import Test
from .forms import TestForm
# Create your views here.
def homepage(request):
    return render(request,"home/home.html")

def aboutpage(request):
    return render(request,"home/about.html")

def servicespage(request):
    return render(request,"home/services.html")

def portfoliopage(request):
    return render(request,"home/portfolio.html")

def teampage(request):
    return render(request,"home/team.html")

def contactpage(request):
    return render(request,"home/contact.html")

def formpage(request):
    return render(request,"home/form.html")

from django.shortcuts import render, redirect
from .forms import TestForm

def testpage(request):
    if request.method == 'POST':
        fm = TestForm(request.POST, request.FILES)  # Pass POST data and files
        if fm.is_valid():
            fm.save()  # Save the form data to the database
            fm = TestForm()
            #return redirect('success_page')  # Redirect to a success page or another page
    else:
        fm = TestForm()  # Create a blank form for GET requests

    return render(request, "home/test.html", {'form': fm})
    

    """
    if request.method == 'POST':
        fm=TestForm(request.POST)
        if fm.is_valid():
            #process the cleaned data
            firstname=fm.cleaned_data['firstname']
            lastname=fm.cleaned_data['lastname']
            return HttpResponse(f"Submitted Sucessfully")
    else:
        fm=TestForm(request.POST or None)
        return render(request,'home/test.html',{'form':fm})
        
        this is manually process to send data from html form to bd
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        phnumber=request.POST.get('phone')
        mail=request.POST.get('email')
        pwd=request.POST.get('password')
        pa=request.POST.get('paddress')
        ta=request.POST.get('taddress')
        spradesh=request.POST.get('selectpradesh')
        gen=request.POST.get('gender')
        msg=request.POST.get('message')
        file=request.POST.get('file')
        cbox=request.POST.get('checkbox')
        icbox=request.POST.get('stream')
        
        

        fm=Test(firstname=fname,lastname=lname,number=phnumber,email=mail,password=pwd,paddress=pa,taddress=ta,selectpradesh=spradesh,gender=gen,message=msg,file=file,checkbox=cbox,inlinecheckbox=icbox)
        fm.save()
    return render(request,"home/test.html")
    """

