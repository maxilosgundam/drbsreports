from django.shortcuts import render

# Create your views here.
#create a new function for every new page
def home(request):
	return render(request,"home.html",{})

def about(request):
	return render(request,"about.html",{})	