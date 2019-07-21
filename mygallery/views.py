from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Location,Category,Image

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request, 'index.html', {"all_images":images})


def search_results(request):

    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html', {"message": message, "all_images": searched_image})

    else:
        message = "You haven't searched for any thing"
        return render(request, 'index.html', {"message": message})


def get_category(request):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request, 'index.html', {'category_results': category_results, 'location_results': location_results})


def get_location(request):
    category_results = Category.objects.all()
    location_results = Location.objects.all()
    return render(request, 'index.html', { 'category_results': category_results, 'location_results': location_results})


       



    
    
