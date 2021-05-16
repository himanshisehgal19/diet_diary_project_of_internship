from django.shortcuts import render,HttpResponse
from basic_app.models import food_diary,meal
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


def continental(request):
    allFood=food_diary.objects.all()
    Continental=food_diary.objects.filter(food_type='Continental')
    paginator=Paginator(Continental,10)
    page=request.GET.get('page')
    try:
        Continental=paginator.page(page)
    except PageNotAnInteger:
        Continental=paginator.page(1)
    except EmptyPage:
        Continental=paginator.page(page.num_pages)
    
    context_dict={'allFood':allFood,'Continental':Continental,'page':page}
    return render(request,'food.html',context=context_dict) 

def north(request):
    north_indian=food_diary.objects.filter(food_type='North')
    result=meal.objects.all()
    paginator=Paginator(north_indian,10)
    page=request.GET.get('page')
    try:
        north_indian=paginator.page(page)
    except PageNotAnInteger:
        north_indian=paginator.page(1)
    except EmptyPage:
        north_indian=paginator.page(page.num_pages)
    
    context_dict={'north_indian':north_indian,'result':result,'page':page}
    return render(request,'north.html',context=context_dict)    

def south(request):
    south_indian=food_diary.objects.filter(food_type='South Indian Food')
    print(south_indian)
    paginator=Paginator(south_indian,10)
    page=request.GET.get('page')
    try:
        south_indian=paginator.page(page)
    except PageNotAnInteger:
        south_indian=paginator.page(1)
    except EmptyPage:
        south_indian=paginator.page(page.num_pages)
    context_dict={'south_indian':south_indian,'page':page}
    return render(request,'south.html',context=context_dict)
    
def search(request):
    query=request.GET['query']
    if len(query)>100:
        allFood=food_diary.objects.none()
    else:
        allFood=food_diary.objects.filter(food_name__icontains=query)
    if allFood.count()==0:
        messages.error(request,"Please fill the correct food item")
    
    params={'allFood':allFood,'query':query}
    return render(request,'search.html',params)
def chinese(request):
    chinese=food_diary.objects.filter(food_type='Chinese')
    paginator=Paginator(chinese,10)
    page=request.GET.get('page')
    try:
        chinese=paginator.page(page)
    except PageNotAnInteger:
        chinese=paginator.page(1)
    except EmptyPage:
        chinese=paginator.page(page.num_pages)
    context_dict={'chinese':chinese,'page':page}
    return render(request,'chinese.html',context=context_dict)
def dessert(request):
    dessert=food_diary.objects.filter(food_type='Sweet Dish')
    
    paginator=Paginator(dessert,10)
    page=request.GET.get('page')
    try:
        dessert=paginator.page(page)
    except PageNotAnInteger:
        dessert=paginator.page(1)
    except EmptyPage:
        dessert=paginator.page(page.num_pages)
    context_dict={'dessert':dessert,'page':page}
    return render(request,'dessert.html',context=context_dict)
    
