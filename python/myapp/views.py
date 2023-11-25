from django.shortcuts import render

def aboutus_views(request):
    return render(request, 'about.html') 

def contactus_views(request):
    return render(request, 'contactus.html') 

def gallery_views(request):
    return render(request, 'gallery.html')

def home_views(request):
    return render(request, 'home.html')

def ourservices_views(request):
    return render(request, 'ourservices.html')


